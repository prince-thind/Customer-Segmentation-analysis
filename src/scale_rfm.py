from sklearn.preprocessing import StandardScaler

def scale_rfm(rfm_df):
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_df[['Recency', 'Frequency', 'Monetary']])
    return rfm_scaled

