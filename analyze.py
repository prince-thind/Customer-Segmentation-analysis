import pandas as pd

# Load the dataset
df = pd.read_csv('./data/data.csv', encoding='ISO-8859-1')

# Data Cleaning: Handle missing values
df.dropna(subset=['CustomerID'], inplace=True)

# Convert 'InvoiceDate' to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Recency: Calculate the number of days since the last purchase
current_date = df['InvoiceDate'].max()
df['Recency'] = (current_date - df['InvoiceDate']).dt.days

# Frequency: Count the number of transactions per customer
frequency = df.groupby('CustomerID')['InvoiceNo'].count().reset_index()
frequency.columns = ['CustomerID', 'Frequency']

# Monetary: Calculate the total amount spent by each customer
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
monetary = df.groupby('CustomerID')['TotalAmount'].sum().reset_index()
monetary.columns = ['CustomerID', 'Monetary']

# Combine Recency, Frequency, and Monetary into a DataFrame
rfm_df = df[['CustomerID', 'Recency']].drop_duplicates().merge(frequency, on='CustomerID').merge(monetary, on='CustomerID')

# Save the RFM data to inspect it
rfm_df.to_csv('./output/rfm_data_commit3.csv', index=False)