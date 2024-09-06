import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# load and clean data
def load_and_clean_data(filepath):
    df = pd.read_csv(filepath, encoding='ISO-8859-1')
    df.dropna(subset=['CustomerID'], inplace=True)
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%y %H:%M')
    return df

# calculate recency
def calculate_recency(df):
    current_date = df['InvoiceDate'].max()
    df['Recency'] = (current_date - df['InvoiceDate']).dt.days
    return df

# calculate frequency
def calculate_frequency(df):
    frequency = df.groupby('CustomerID')['InvoiceNo'].count().reset_index()
    frequency.columns = ['CustomerID', 'Frequency']
    return frequency

# calculate monetary value
def calculate_monetary(df):
    df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
    monetary = df.groupby('CustomerID')['TotalAmount'].sum().reset_index()
    monetary.columns = ['CustomerID', 'Monetary']
    return monetary

# merge recency, frequency, and monetary
def merge_rfm(df, frequency, monetary):
    df = df.sort_values(by=['CustomerID', 'InvoiceDate'], ascending=[True, False])
    rfm_df = df[['CustomerID', 'Recency']].drop_duplicates().merge(frequency, on='CustomerID').merge(monetary, on='CustomerID')
    return rfm_df

# scale RFM values
def scale_rfm(rfm_df):
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_df[['Recency', 'Frequency', 'Monetary']])
    return rfm_scaled

# apply K-Means clustering
def apply_kmeans(rfm_scaled, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(rfm_scaled)
    return kmeans

# save data and plot
def save_data_and_plot(rfm_df, kmeans):
    rfm_df['Cluster'] = kmeans.labels_
    rfm_df.to_csv('./output/clustered_data.csv', index=False)
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Recency', y='Monetary', hue='Cluster', data=rfm_df, palette='viridis')
    plt.title('Customer Segments')
    plt.savefig('./output/customer_segments_plot.png')

def main(filepath):
    df = load_and_clean_data(filepath)
    df = calculate_recency(df)
    frequency = calculate_frequency(df)
    monetary = calculate_monetary(df)
    rfm_df = merge_rfm(df, frequency, monetary)
    rfm_df.to_csv('./output/rfm_data.csv', index=False)
    
    rfm_scaled = scale_rfm(rfm_df)
    kmeans = apply_kmeans(rfm_scaled)
    
    save_data_and_plot(rfm_df, kmeans)
    print("Final plot and clustered data saved.")

main('./data/data.csv')
