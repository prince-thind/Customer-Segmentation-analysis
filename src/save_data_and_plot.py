import matplotlib.pyplot as plt
import seaborn as sns

def save_data_and_plot(rfm_df, kmeans):
    rfm_df['Cluster'] = kmeans.labels_
    rfm_df.to_csv('./output/clustered_data.csv', index=False)
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Recency', y='Monetary', hue='Cluster', data=rfm_df, palette='viridis')
    plt.title('Customer Segments')
    plt.savefig('./output/customer_segments_plot.png')

