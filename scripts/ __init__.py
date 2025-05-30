import pandas as pd


#loaded Data
file_path = '../Data/raw_analyst_ratings.csv'

df = pd.read_csv(file_path)


def robust_to_datetime(series):
    converted_series = []
    for value in series:
        try:
            converted_value = pd.to_datetime(value)
            converted_series.append(converted_value)
        except ValueError:
            converted_series.append(value)
    return pd.Series(converted_series)

# Assuming your DataFrame is called 'df' and the column is 'date'
# Replace 'df' with the actual name of your DataFrame
df['date'] = robust_to_datetime(df['date'])

# Now, let's check the data types in the 'date' column again
def check_column_data_types(series):
    types = set()
    for item in series:
        types.add(type(item))
    return types

data_types_after_conversion = check_column_data_types(df['date'])
print(f"The data types present in 'date' after attempted conversion are: {data_types_after_conversion}")
print(df['date'].head())