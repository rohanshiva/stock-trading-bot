import pandas as pd

# The goal of this program is to extract this week's top gaining stocks from Yahoo Finance

# Getting data from Yahoo Fiance and filtering the data frame for the top five gainers
stocks = []
data = pd.read_html("https://finance.yahoo.com/gainers")
data = data[0]
data = data.head(5)
data = data['Symbol']

# Appends the empty stock list with the top five gainers from the data frame
for i in range(0, 5):
    stocks.append(data[i])

# testing
print(stocks)
