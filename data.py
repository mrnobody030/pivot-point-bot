from twelvedata import TDClient
from requests.exceptions import ConnectionError

try:
    td = TDClient(apikey="8c64c253899f4ea2bf2015314052ee3e")

    ts = td.time_series(
        symbol="USD/JPY",
        exchange="Huobi",
        interval="1day",#this is the candles time frame
        outputsize=3,#this is how many candle will return
        timezone="America/New_York"
    )

    data = ts.with_atr().as_pandas()

except ConnectionError:
    print("nice")

