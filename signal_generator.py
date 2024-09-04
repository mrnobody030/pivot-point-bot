from time import sleep
from twelvedata import TDClient

def signal_generator(symbol,pivote_point):
    td = TDClient(apikey="8c64c253899f4ea2bf2015314052ee3e")
    rp = td.time_series(
        symbol=symbol,
        exchange="Huobi",
        interval="15min",
        outputsize=1,
        timezone="America/New_York"
    )

    now = rp.as_pandas().index[0]
    real_price = rp.as_pandas().loc[now].loc["close"]

    if pivote_point + (pivote_point*0.001) > real_price > pivote_point - (pivote_point*0.001) :
        print("THE TIME HAS COME")

    print("NOT YET " + symbol)
    sleep(15)
