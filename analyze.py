import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

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

# Save the RFM data for inspection
rfm_df.to_csv('./output/rfm_data.csv', index=False)

# Data Scaling: Scale the RFM values
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_df[['Recency', 'Frequency', 'Monetary']])

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(rfm_scaled)

# Add the cluster labels to the RFM DataFrame
rfm_df['Cluster'] = kmeans.labels_

# Save the clustered data for inspection
rfm_df.to_csv('./output/clustered_data.csv', index=False)

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Recency', y='Monetary', hue='Cluster', data=rfm_df, palette='viridis')
plt.title('Customer Segments')

# Save the plot to a file
plt.savefig('./output/customer_segments_plot.png')

# Save the final clustered data to a CSV file
rfm_df.to_csv('./output/customer_segments_output.csv', index=False)

print("Final plot and clustered data saved.")
