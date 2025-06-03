import pandas as pd

def align_dates(stock_df: pd.DataFrame, news_df: pd.DataFrame) -> pd.DataFrame:
    """
    Align stock data and news data by date.
    Assumes stock_df indexed by Date and news_df has a 'Date' column.
    Merges news sentiment (or other news info) aggregated by date with stock data.

    :param stock_df: DataFrame with stock data indexed by Date.
    :param news_df: DataFrame with news data, must have 'Date' and 'sentiment' columns.
    :return: DataFrame merged on date with stock data and aggregated news sentiment.
    """
    # Ensure 'Date' is datetime in news_df
    news_df['Date'] = pd.to_datetime(news_df['Date'])

    # Aggregate news sentiment by date (mean sentiment for all news on that date)
    news_daily = news_df.groupby('Date')['sentiment'].mean().reset_index()

    # Align dates: join stock data with news sentiment on Date
    # stock_df expected to have Date as index; reset index to merge
    stock_reset = stock_df.reset_index()

    merged_df = pd.merge(stock_reset, news_daily, how='left', on='Date')

    # Fill missing sentiment values with 0 (or NaN, depending on your choice)
    merged_df['sentiment'].fillna(0, inplace=True)

    # Set Date back as index
    merged_df.set_index('Date', inplace=True)

    return merged_df
