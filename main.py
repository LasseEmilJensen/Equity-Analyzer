import yfinance as yf

print("=" * 40)
print("     Equity Analyzer")
print("=" * 40)

ticker = input("Enter ticker: ")

stock = yf.Ticker(ticker)

info = stock.info

print("\nCompany:", info.get("longName"))
print("Current Price:", info.get("currentPrice"))
print("Currency:", info.get("currency"))
