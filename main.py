from twelvedata import TDClient

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
################################################# APP ####################################################################

def stratigy(symbol):

########################################################### GET DATA #####################################################

    td = TDClient(apikey="8c64c253899f4ea2bf2015314052ee3e")

    ts = td.time_series(
        symbol=symbol,
        exchange="Huobi",
        interval="1day",
        outputsize=3,
        timezone="America/New_York"
    )

    print(symbol)
    data = ts.with_atr().as_pandas()
    yesterday = data.index[1]
    print(yesterday)
    pivote_point = (data.loc[yesterday].loc["high"] + data.loc[yesterday].loc["low"] + data.loc[yesterday].loc["close"]) / 3

##########################################################################################################################
########################################################### FIRST CONDITION ##############################################
#this section will check if the candle is green or red and the upper and lower shadows
    if data.loc[yesterday].loc["close"] > data.loc[yesterday].loc["open"]:#green candle
        if (data.loc[yesterday].loc["high"] - data.loc[yesterday].loc["close"]) > 0.1 * abs(data.loc[yesterday].loc["open"]-data.loc[yesterday].loc["close"]):
            print("It is a green candle and also has upper shadow there for the first cendetion is not satecfied")
            result = "It is a green candle and also has upper shadow there for the first cendetion is not satecfied"
            return False, result

        elif data.loc[yesterday].loc["close"] < pivote_point :
            print ("the price is above the pivote point and there is no place to buy")
            result = "the price is above the pivote point and there is no place to buy"
            return False, result

    elif data.loc[yesterday].loc["close"] < data.loc[yesterday].loc["open"]:#red candle
        if (data.loc[yesterday].loc["close"] - data.loc[yesterday].loc["low"]) > 0.1* abs(data.loc[yesterday].loc["open"]-data.loc[yesterday].loc["close"]) :
            print("It is a red candle and also has lower shadow there for the first cendetion is not satecfied")
            result = "It is a red candle and also has lower shadow there for the first cendetion is not satecfied"
            return False, result

        elif data.loc[yesterday].loc["close"] > pivote_point :
            print ("the price is below the pivote point and there is no place to sell")
            result = "the price is below the pivote point and there is no place to sell"
            return False, result

##########################################################################################################################
####################################################### SECOND CONDETION #################################################
#here it checks if the range of yesterdays candle is atlist 8/10 or higher then ATR(Avrage True Range)
    if data.loc[yesterday].loc["atr"]*8/10 > abs(data.loc[yesterday].loc["open"] - data.loc[yesterday].loc["close"]):
        print("second condetion is not satecfied")
        result = "second condetion is not satecfied"
        return False, result
    return True , pivote_point 

##########################################################################################################################