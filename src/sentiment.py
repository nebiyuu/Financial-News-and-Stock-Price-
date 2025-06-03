import pandas as pd
from textblob import TextBlob

#calculate sentiment
def calculate_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Applying the sentiment analysis function to your headlines
df['Sentiment'] = df['headline'].apply(calculate_sentiment)