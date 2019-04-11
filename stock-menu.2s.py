#!/usr/bin/env python

import json, urllib2, os

def get_stock_price(stock):
	response = urllib2.urlopen('https://api.iextrading.com/1.0/stock/' + stock + '/quote')
	return json.loads(response.read())

def create_output_string(stock, url):
	output = stock
	output += " - $"
	output += "{:0.2f}".format(response["latestPrice"])
	output += " (" + "{:0.2f}".format(response["changePercent"] * 100.00) + "%)"

        color = "#f45531" if response["changePercent"] < 0 else "#21ce99"

        if(url):
            quote_url = 'https://www.finance.yahoo.com/quote/' + stock
            output += " | color=" + color + " href=" + quote_url
        else:
            output += " | color=" + color

	return output


path = os.path.dirname(os.path.abspath(__file__))
f = open(path + "/stocks/stocks.txt")
stocks = f.read().split(',')
del stocks[len(stocks) - 1]
f.close()

response = get_stock_price(stocks[0])
print create_output_string(stocks[0], False)
print '---'

newLine = ""

for stock in stocks:
    response = get_stock_price(stock)
    print create_output_string(stock, True)

for x in range(1, len(stocks)):
    newLine += stocks[x] + ","
newLine += stocks[0] + ","

f = open(path + "/stocks/stocks.txt", "w")
f.write(newLine)
f.close

