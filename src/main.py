from load_and_clean_data import load_and_clean_data
from calculate_recency import calculate_recency
from calculate_frequency import calculate_frequency
from calculate_monetary import calculate_monetary
from merge_rfm import merge_rfm
from scale_rfm import scale_rfm
from apply_kmeans import apply_kmeans
from save_data_and_plot import save_data_and_plot

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
    print('Final plot and clustered data saved.')

if __name__ == '__main__':
    main('./data/data.csv')

