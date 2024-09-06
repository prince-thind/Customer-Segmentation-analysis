def calculate_recency(df):
    current_date = df['InvoiceDate'].max()
    df['Recency'] = (current_date - df['InvoiceDate']).dt.days
    return df

