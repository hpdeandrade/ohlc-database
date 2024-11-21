import pandas as pd
import pytz
import yfinance as yf

print(f"\u001b[44;1mYahoo: ONLINE\033[0m")

class Yahoo:

    @staticmethod
    def Download(symbol, tzone, start, final):
        data = yf.download(symbol, interval="5m", start=start, end=final, multi_level_index=False)
        df = pd.DataFrame(data)
        if not df.empty:
            df.index.name = "DATETIME"
            df.rename(columns={"Open": "OPEN","High": "HIGH", "Low": "LOW", "Adj Close": "CLOSE", "Volume": "VOLUME"}, inplace=True)
            df.drop(columns=["Close"], inplace=True)
            df.reset_index(inplace=True)
            df["DATETIME"] = df["DATETIME"].dt.tz_convert(pytz.timezone(tzone)).dt.tz_localize(None)
            df["DATETIME"] = pd.to_datetime(df["DATETIME"], unit="s").astype("datetime64[s]")
        return df