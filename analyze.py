import pandas as pd

# Load the dataset
df = pd.read_csv('./data/data.csv', encoding='ISO-8859-1')

# Data Cleaning: Handle missing values for CustomerID
df.dropna(subset=['CustomerID'], inplace=True)

# Convert 'InvoiceDate' to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Feature Engineering: Recency
current_date = df['InvoiceDate'].max()
df['Recency'] = (current_date - df['InvoiceDate']).dt.days

# Save the cleaned and processed data to check the recency feature
df[['CustomerID', 'Recency']].to_csv('./output/processed_data_commit2.csv', index=False)

print("Data cleaning and Recency feature created.")
