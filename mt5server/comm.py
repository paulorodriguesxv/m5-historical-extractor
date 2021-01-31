import pandas as pd
import MetaTrader5 as mt5

# connect to MetaTrader 5
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()


def get_stock_by_bars(stocks, bars, timeframe):
    """ get prices for N number os periods """
    data = None
    for i, stock in enumerate(stocks):

        # get prices from MT5
        rates = mt5.copy_rates_from_pos(stock, timeframe, 0, bars)
        rates_frame = pd.DataFrame(rates)
        # convert timestamp
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

        # creates a new dataframe with all each stock
        rates_frame['stock'] = stock

        if i == 0:
            data = rates_frame
        else:
            data = data.append(rates_frame)

    return data


def get_stock_by_date(stocks, start_date, end_date, timeframe):
    """ get prices between a start and end period """
    data = None
    for i, stock in enumerate(stocks):
        #rates = mt5.copy_rates_from_pos(stock, timeframe, 0, bars)
        rates = mt5.copy_rates_range(stock, timeframe, start_date, end_date)
        rates_frame = pd.DataFrame(rates)
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        rates_frame['stock'] = stock

        if i == 0:
            data = rates_frame
        else:
            data = data.append(rates_frame)

    return data