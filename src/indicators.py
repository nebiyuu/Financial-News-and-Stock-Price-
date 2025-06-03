import talib

def add_ta_indicators(df):
    """
    Add technical indicators to the DataFrame.
    :param df: DataFrame with stock data.
    :return: DataFrame with added indicators.
    """
    # Simple Moving Averages (SMA)
    df["SMA_10"] = talib.SMA(df["Close"], timeperiod=10)
    df["SMA_50"] = talib.SMA(df["Close"], timeperiod=50)
    
    # Exponential Moving Averages (EMA)
    df["EMA_10"] = talib.EMA(df["Close"], timeperiod=10)
    
    # Relative Strength Index (RSI)
    df["RSI"] = talib.RSI(df["Close"], timeperiod=14)
    
    # MACD
    df["MACD"], df["MACD_Signal"], df["MACD_Hist"] = talib.MACD(
        df["Close"], fastperiod=12, slowperiod=26, signalperiod=9
    )
    # Bollinger Bands - standard 20 period with 2 standard deviations
    upper, middle, lower = talib.BBANDS(
        df["Close"],
        timeperiod=20,  # period for the bands
        nbdevup=2,      # upper band standard deviations
        nbdevdn=2,      # lower band standard deviations
        matype=0        # 0 = SMA, 1 = EMA, etc.
    )
    df['BB_upper'] = upper
    df['BB_middle'] = middle
    df['BB_lower'] = lower

    return df

