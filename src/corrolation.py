import pandas as pd
import numpy as np
from textblob import TextBlob
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# 1. Load and prepare news data
def load_news_data(news_file):
    """Load news data and preprocess dates"""
    news_df = pd.read_csv(news_file)
    
    # Convert to datetime and normalize to date only
    news_df['date'] = pd.to_datetime(news_df['date']).dt.normalize()
    
    # Drop duplicates and sort
    news_df = news_df.drop_duplicates().sort_values('date')
    
    return news_df

# 2. Load and prepare stock data
def load_stock_data(stock_file):
    """Load stock data and calculate daily returns"""
    stock_df = pd.read_csv(stock_file)
    
    # Convert to datetime and normalize to date only
    stock_df['date'] = pd.to_datetime(stock_df['date']).dt.normalize()
    
    # Calculate daily percentage returns
    stock_df['daily_return'] = stock_df['close'].pct_change() * 100
    
    # Drop NA values from returns calculation
    stock_df = stock_df.dropna(subset=['daily_return'])
    
    return stock_df

# 3. Perform sentiment analysis
def analyze_sentiment(headline):
    """Analyze sentiment of a single headline using TextBlob"""
    analysis = TextBlob(headline)
    return analysis.sentiment.polarity

def add_sentiment_scores(news_df):
    """Add sentiment scores to news dataframe"""
    news_df['sentiment'] = news_df['headline'].apply(analyze_sentiment)
    return news_df

# 4. Aggregate and correlate data
def aggregate_and_correlate(news_df, stock_df):
    """Aggregate sentiment by date and correlate with stock returns"""
    # Aggregate sentiment scores by date
    daily_sentiment = news_df.groupby('date')['sentiment'].mean().reset_index()
    
    # Merge with stock data
    merged_df = pd.merge(daily_sentiment, stock_df, on='date', how='inner')
    
    # Calculate correlation
    correlation, p_value = pearsonr(merged_df['sentiment'], merged_df['daily_return'])
    
    return merged_df, correlation, p_value

# 5. Visualization
def plot_correlation(merged_df, correlation, p_value, ticker):
    """Plot sentiment vs returns with correlation results"""
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_df['sentiment'], merged_df['daily_return'], alpha=0.5)
    plt.title(f'Sentiment vs Daily Returns for {ticker}\nCorrelation: {correlation:.2f} (p-value: {p_value:.4f})')
    plt.xlabel('Average Daily Sentiment Score')
    plt.ylabel('Daily Return (%)')
    plt.grid(True)
    plt.savefig(f'sentiment_vs_returns_{ticker}.png')
    plt.close()

def main():
    # Configuration - update these paths
    news_file = 'data/news_data.csv'
    stock_file = 'data/stock_prices.csv'
    ticker = 'AAPL'  # Example ticker
    
    # Load and process data
    print("Loading and processing news data...")
    news_df = load_news_data(news_file)
    news_df = add_sentiment_scores(news_df)
    
    print("Loading and processing stock data...")
    stock_df = load_stock_data(stock_file)
    
    # Aggregate and correlate
    print("Analyzing correlation...")
    merged_df, correlation, p_value = aggregate_and_correlate(news_df, stock_df)
    
    # Output results
    print(f"\nResults for {ticker}:")
    print(f"Correlation between sentiment and returns: {correlation:.2f}")
    print(f"P-value: {p_value:.4f}")
    
    # Save visualization
    plot_correlation(merged_df, correlation, p_value, ticker)
    print("Visualization saved to current directory.")

if __name__ == "__main__":
    main()