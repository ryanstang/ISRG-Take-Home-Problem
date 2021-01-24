"""
Intuitive Surgical Take-Home Problem
Description: Write a Python application that can scrap stock price data from a public
website (e.g. yahoo finance, https://finance.yahoo.com/quote/ISRG/history?p=ISRG) 
so that when givena stock tick symbol (e.g. “ISRG”, aka Intuitive Surgical) as the input,
the application returns the stock’s high, low, open and close prices today.
Author: Ryan Tang
"""
from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq

# asking user what stock user wants to see and creating the URL
stock = input("What stock do you need data from?\nStock Symbol: ")
myUrl = "https://finance.yahoo.com/quote/" + stock + "/history?p=" + stock

# opening up connection and grabbing page
uClient = uReq(myUrl)
pageHTML = uClient.read()

# close client
uClient.close()

#html parsing
pageSoup = soup(pageHTML, "html.parser")

# find all data for the stock
data = pageSoup.find_all("tr", {"class": "BdT"})

# get data for current day
currentDay = data[0]

# initialize terms and dictionary for the data
infoKeys = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
info = {}

# enumerate over data for given stock on current day
for i, num in enumerate(currentDay.find_all("td")):
    info[infoKeys[i]] = num.text

# print out date, open, highm low, close for given stock
print('\n{:>11}'.format(stock))
print("Date:{:>13}".format(info["Date"]))
print("Open:{:>13}".format(info["Open"]))
print("High:{:>13}".format(info["High"]))
print("Low:{:>14}".format(info["Low"]))
print("Close:{:>12}".format(info["Close"]))

