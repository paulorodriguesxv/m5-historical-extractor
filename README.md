# Metatrader5 stock REST Server

It's a super simle sample :-)

Please, read the article at https://codekraft.com.br/how-get-stock-price-data-from-your-brazilian-broker-mt5-rodrigues/ to know how to use

To run:
 - uvicorn mt5server.main:app --reload --loop asyncio

Request:
 - http://127.0.0.1:8000/quotes/petr4/daily

Swagger:
 - http://localhost:8000/docs

# Star if you like it.
If you like or use this project, consider showing your support by starring it.

# Contributing
 
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D3


## Credits
 
Developer - Paulo Rodrigues (@paulorodriguesxv)

## License
 
The MIT License (MIT)

Copyright (c) 2021 Paulo Rodrigues

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
