def calculate_monetary(df):
    df['TotalAmount'] = df['Quantity'] * df['UnitPrice']
    monetary = df.groupby('CustomerID')['TotalAmount'].sum().reset_index()
    monetary.columns = ['CustomerID', 'Monetary']
    return monetary

