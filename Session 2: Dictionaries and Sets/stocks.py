"""
Create a program that includes a dictionary of stocks. Your dictionary should consist of at least 10 ticker symbols. The key should be the stock ticker symbol, and the value should be the stock’s current price (the values can be fictional). Ask the user to enter a ticker symbol. Your program will search the dictionary for the ticker symbol and then print the ticker symbol and the stock price. If the ticker symbol is not located, print a message indicating that the ticker symbol was not found.

Use: dict = stocks

ticker input (ask the user for a “fictional” ticker symbol)

"""
import pandas as pd

# Dictionary of stocks (fictional prices)
stocks = {
    "AAPL": 178.55,
    "MSFT": 315.20,
    "GOOG": 140.75,
    "AMZN": 132.80,
    "TSLA": 245.60,
    "NFLX": 395.45,
    "NVDA": 420.30,
    "META": 290.10,
    "DIS": 92.40,
    "IBM": 145.75
}

# ✅ Convert dictionary to DataFrame properly
df = pd.DataFrame(list(stocks.items()), columns=["Ticker", "Price"])
print(df['Ticker'])

# Ask the user for a ticker symbol
ticker = input("Enter a ticker symbol (e.g., AAPL, TSLA): ").upper()

# Search for the ticker in the dictionary
if ticker in stocks:
    print(f"Ticker: {ticker} | Price: ${stocks[ticker]}")
else:
    print(f"Ticker symbol '{ticker}' was not found in the database.")
