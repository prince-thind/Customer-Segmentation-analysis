import pandas as pd

# Load the dataset from ./data/data.csv
df = pd.read_csv('./data/data.csv', encoding='ISO-8859-1')

# Print the first few rows to inspect the data
print(df.head())
