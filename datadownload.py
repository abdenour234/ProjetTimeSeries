import yfinance as yf

df=yf.download(tickers="AAPL",period="10y")

df.to_csv("Data.csv")