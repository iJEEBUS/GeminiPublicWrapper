'''
	Filename: gemini.py
	Author: Ronald Rounsifer
	Date created: 10/23/2017
	Date last modified: 10/24/2017
	Python version 2.7.13
'''
import requests

def setSandbox(input):
	if input:
		url = 'https://api.sandbox.gemini.com/v1'
	else:
		url = 'https://api.gemini.com/v1'
	return url

"""
Retrieves all available symbols for trading
"""
def getExchanges(url):
	exchanges = requests.get(url + "/symbols").json()
	return exchanges

"""
Returns the ask, bid, volume, and last price sold of a specified ticker
"""
def getTickerInformation(ticker):
	info = requests.get(_url + "/pubticker/" + ticker).json()
	return info

"""
Returns the lowest ask currently available
"""
def getAsk(ticker):
	ask = requests.get(_url + "/pubticker/" + ticker).json()['ask']
	return ask

"""
Returns information about the 24 hour volume on the exchange
"""
def getVolume(ticker):
	volume = requests.get(_url + "/pubticker/" + ticker).json()['volume']
	return volume

"""
Returns the highest bid currently available
"""
def getBid(ticker):
	bid = requests.get(_url + "/pubticker/" + ticker).json()['bid']
	return bid

"""
Returns the price of the last executed trade
"""
def getLast(ticker):
	last = requests.get(_url + "/pubticker/" + ticker).json()['last']
	return last

"""
Returns the current order book, as two arrays, one of bids, and one of asks.

Parameters include: limit_bids, 
					limit_asks.

Returns: bids array [price, amount, timestamp], 
		 asks array [price, amount, timestamp]

"""

## HAVE A VARIABLE FOR EACH PARAMETER, TAKE THEIR VALUES AS ARGUMENTS
def getCurrentOrderBook(ticker, *limit):

	if params:
		url_with_parameters = _url + '/book/' + ticker
		url_with_parameters = addParameters(url_with_parameters, params)
		order_book = requests.get(url_with_parameters).json()
		print url_with_parameters
	else:
		order_book = requests.get(_url + "/book/" + ticker).json()
	return order_book


"""
This will return the trades that have executed since the specified timestamp. 
Timestamps are either seconds or milliseconds since the epoch (1970-01-01). 
See the Data Types section about timestamp for information on this.

Each request will show at most 500 records.

If no since or timestamp is specified, then it will show the most recent trades; otherwise, 
it will show the most recent trades that occurred after that timestamp.
"""
def getTradeHistory(ticker, *params):

	if params:
		url_with_parameters = _url + '/trades/' + ticker
		url_with_parameters = addParameters(url_with_parameters, params)
		order_book = requests.get(url_with_parameters).json()
		#print url_with_parameters
	else:
		order_book = requests.get(_url + '/trades/' + ticker).json()
	return order_book

"""
This will return the auction events, optionally including publications of indicative prices.
"""
def getCurrentAuction(ticker):
	current_auction = requests.get(_url + '/auction/' + ticker).json()
	return current_auction



def getAuctionHistory(ticker):
	auction_history = requests.get(_url + '/auction/' + ticker + '/history').json()
	return auction_history


"""
Add GET params to provided URL being aware of existing.

    url = 'https://api.gemini.com/v1'
    >> new_params = {'limit_asks': 2, 'limit_bids': 2}
    >> add_url_params(url, new_params)
    'https://api.gemini.com/v1/ethusd?limit_asks=2&limit_bids=2'
"""
def addParameters(url, params):
	url = url + '?'
	for x in params:
		print params[x]
		#url = url + x + '=%s&' % (params[x])
	return url[:-1]


"""
Returns the dictionary of all of the functions available for public use.
"""
def getHelp():
	functions = {'getHelp()': 'Returns the dictionary of all of the functions available for public use.',
				'help(*method)': '\n       Used to show all of the available functions along with the definitions of each function.',
				'getExchanges(url) ': 'getExchanges(): \n       Retrieves all available symbols for trading',
				'getTickerInformation(ticker) ': 'getTickerInformation(): \n       Returns the ask, bid, volume, and last price sold of a specified ticker',
				'getAsk(ticker)': 'getAsk(): \n       Returns the lowest ask currently available', 
				'getVolume(ticker)': 'getVolume(): \n       Returns information about the 24 hour volume on the exchange',
				'getBid(ticker)': 'getBid(): \n       Returns the highest bid currently available',
				'getLast(ticker)': 'getLast(): \n       Returns the price of the last executed trade',
				'getCurrentOrderBook(ticker)': 'getCurrentOrderBook(): \n       Returns the current order book, as two arrays, one of bids, and one of asks',
				'getTradeHistory(ticker, *limit)': 'getTradeHistory(): \n       This will return the trades that have executed since the specified timestamp. If no since or timestamp is specified, then it will show the most recent trades; otherwise, it will show the most recent trades that occurred after that timestamp.',
				'getCurrentAuction(ticker)': 'getCurrentAuction(): \n       This will return the auction events, optionally including publications of indicative prices',
				'getAuctionHistory(ticker)': 'getAuctionHistory(): \n       This will return the auction events, optionally including publications of indicative prices, since the specific timestamp'}
	return functions


"""
Used to show all of the available functions along with the definitions of each function.
Can specify a single function as long as it is passed as an argument.
Returns nothing.
"""
def help(*method):
	functions = {'help(*method)': '\n       Used to show all of the available functions along with the definitions of each function.',
				'getExchanges(url): ': 'getExchanges(): \n       Retrieves all available symbols for trading',
				'getTickerInformation(ticker): ': 'getTickerInformation(): \n       Returns the ask, bid, volume, and last price sold of a specified ticker',
				'getAsk(ticker)': 'getAsk(): \n       Returns the lowest ask currently available', 
				'getVolume(ticker)': 'getVolume(): \n       Returns information about the 24 hour volume on the exchange',
				'getBid(ticker)': 'getBid(): \n       Returns the highest bid currently available',
				'getLast(ticker)': 'getLast(): \n       Returns the price of the last executed trade',
				'getCurrentOrderBook(ticker)': 'getCurrentOrderBook(): \n       Returns the current order book, as two arrays, one of bids, and one of asks',
				'getTradeHistory(ticker, *limit)': 'getTradeHistory(): \n       This will return the trades that have executed since the specified timestamp. If no since or timestamp is specified, then it will show the most recent trades; otherwise, it will show the most recent trades that occurred after that timestamp.',
				'getCurrentAuction(ticker)': 'getCurrentAuction(): \n       This will return the auction events, optionally including publications of indicative prices',
				'getAuctionHistory(ticker)': 'getAuctionHistory(): \n       This will return the auction events, optionally including publications of indicative prices, since the specific timestamp'}
	if method:
		if method[0] == 'all':
			for x in functions.values():
				print x
		else:
			print functions[method[0]]
	else:
		for x in functions:
			print x
