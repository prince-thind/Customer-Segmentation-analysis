def merge_rfm(df, frequency, monetary):
    df = df.sort_values(by=['CustomerID', 'InvoiceDate'], ascending=[True, False])
    rfm_df = df[['CustomerID', 'Recency']].drop_duplicates().merge(frequency, on='CustomerID').merge(monetary, on='CustomerID')
    return rfm_df

