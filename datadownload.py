import yfinance as yf

df=yf.download(tickers="AAPL",period="5y")

df.to_csv("Data.csv")