import yfinance as yf
import pandas as pd

def analyze_stock(symbol):
    df = yf.download(symbol, period="1mo")

    df["MA_5"] = df["Close"].rolling(5).mean()
    df["Change_%"] = df["Close"].pct_change() * 100

    last_close = df["Close"].iloc[-1]
    last_ma5 = df["MA_5"].iloc[-1]
    last_change = df["Change_%"].iloc[-1]
    last_volume = df["Volume"].iloc[-1]

    if last_close > last_ma5:
        trend = "Above MA5 (Bullish)"
    else:
        trend = "Below MA5 (Bearish)"

    result = {
        "symbol": symbol,
        "close": round(float(last_close), 2),
        "ma5": round(float(last_ma5), 2),
        "change_percent": round(float(last_change), 2),
        "volume": int(last_volume),
        "trend": trend
    }

    return result