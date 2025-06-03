from textblob import TextBlob

def compute_sentiment(news_df):
    """
    Compute sentiment scores for news headlines.
    :param news_df: DataFrame with a 'Headline' column.
    :return: DataFrame with an added 'Sentiment' column.
    """
    if "Headline" not in news_df.columns:
        raise ValueError("The news DataFrame must contain a 'Headline' column.")
    
    def get_sentiment(text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity  # Sentiment score between -1 and 1

    news_df["Sentiment"] = news_df["Headline"].apply(get_sentiment)
    return news_df
