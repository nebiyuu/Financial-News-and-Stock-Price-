# Financial News and Stock Price Analysis

This project analyzes financial news and stock price data to extract insights about analyst ratings, publisher activity, and trends over time.

## Project Structure

.github/
    workflows/
        unittests.yml
.gitignore
requirements.txt
README.md
src/
    __init__.py
notebooks/
    __init__.py
    README.md
tests/
    __init__.py
scripts/
    __init__.py

    
## Getting Started

1. **Install dependencies**  
   Run the following command to install required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

2. **Run the notebook**  
   Open [notebook/describe.ipynb](notebook/describe.ipynb) in Jupyter or VS Code to explore the data and visualizations.

## Data Sources

- `Data/raw_analyst_ratings.csv`: Analyst ratings dataset.
- `Data/yfinance_data/`: Historical stock price data for selected tickers.

## Visualizations

The notebook includes:
- Top headlines and their frequencies
- Article counts per publisher
- Distribution of articles by day of the week and month

## Continuous Integration

Unit tests (if present) are run automatically via [GitHub Actions](.github/workflows/unittest.yml).
