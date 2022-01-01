from datetime import datetime
from enum import Enum
from http import HTTPStatus
from typing import Optional, List
from pydantic import BaseModel

from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.gzip import GZipMiddleware

import MetaTrader5 as mt5

from mt5server.comm import get_stock_by_bars, get_stock_by_date

app = FastAPI()

app.add_middleware(GZipMiddleware, minimum_size=1000)


class TimeframeEnum(str, Enum):
    """ Supported timeframes """
    DAILY = 'daily'
    FIVE_MINUTE = '5_MINUTE'

    @staticmethod
    def list():
        return list(map(lambda c: c.value, TimeframeEnum))


class StockData(BaseModel):
    """ Prices Response model """
    time: datetime
    open: float
    high: float
    low: float
    close: float
    real_volume: Optional[float] = None


class MT5HTTPError(BaseModel):
    """ Custom error message """
    detail: str

    class Config:
        schema_extra = {
            "example": {
                "detail": "Communication with MT5 can't be established."
            },
        }


def ct2mt5(timeframe):
    if timeframe == TimeframeEnum.FIVE_MINUTE:
        return mt5.TIMEFRAME_M5

    return mt5.TIMEFRAME_D1

@app.get("/quotes/{stock}/{timeframe}",
         responses={
             HTTPStatus.OK.value: {
                 "model": List[StockData]
             },
             HTTPStatus.UNPROCESSABLE_ENTITY.value: {
                 "model": MT5HTTPError,
                 "description": "This endpoint always raises an error",
             }
         })
async def root(stock, timeframe: TimeframeEnum, x_start_date: Optional[datetime] = Header(None), x_end_date: Optional[datetime] = Header(None)):

    stock = stock.upper()

    _timeframe = ct2mt5(timeframe)

    if x_start_date and x_end_date:
        prices = get_stock_by_date([stock], x_start_date, x_end_date, _timeframe)
    else:
        prices = get_stock_by_bars([stock], 1000, _timeframe)

    prices = prices[['time', 'open', 'high', 'low', 'close', 'real_volume']]

    prices = prices.to_dict('records')

    return [StockData(**data) for data in prices]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)