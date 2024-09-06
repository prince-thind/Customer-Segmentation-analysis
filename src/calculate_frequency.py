def calculate_frequency(df):
    frequency = df.groupby('CustomerID')['InvoiceNo'].count().reset_index()
    frequency.columns = ['CustomerID', 'Frequency']
    return frequency

