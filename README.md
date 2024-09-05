# **Customer Segmentation Using RFM Analysis and K-Means Clustering**

## **Project Overview**

This project focuses on applying **RFM (Recency, Frequency, Monetary)** analysis combined with **K-Means Clustering** to segment customers based on their purchasing behavior. The goal of this project is to help businesses better understand their customer base and create tailored marketing strategies for different customer segments.

By utilizing RFM analysis, we are able to evaluate customer value based on how recently (Recency) they made a purchase, how frequently (Frequency) they make purchases, and the monetary value (Monetary) they generate. After computing RFM metrics, we applied **K-Means Clustering** to identify distinct customer segments. These segments provide actionable insights into customer behaviors, allowing businesses to target their efforts more effectively.

## **Key Features**

### 1. **Data Cleaning and Preparation**

- Handled missing values by removing records with missing **CustomerID** values to ensure accurate analysis.
- Converted **InvoiceDate** into a usable datetime format to calculate **Recency** metrics.
- Calculated **Recency**, **Frequency**, and **Monetary** metrics, key to RFM analysis:
  - **Recency:** Number of days since the customer's last purchase.
  - **Frequency:** Total number of purchases made by the customer.
  - **Monetary:** Total amount spent by the customer.

### 2. **RFM Analysis**

- Generated an **RFM DataFrame** by calculating the **Recency, Frequency, and Monetary** values for each customer.
- Exported the calculated RFM data for further analysis and inspection.

### 3. **K-Means Clustering**

- Standardized the RFM metrics using **StandardScaler** to ensure all features contribute equally during clustering.
- Applied the **K-Means Clustering** algorithm to group customers into **4 segments**, based on their RFM scores.
- Added the cluster labels to the final DataFrame for better visualization and interpretation of customer segments.

### 4. **Data Visualization**

- Created a scatter plot using **Seaborn** to visualize the clusters. This visualization represents customer segments based on Recency and Monetary values, color-coded by cluster.
- The visualization helps identify distinct customer behaviors and segments, enabling targeted marketing strategies.

### 5. **File Outputs**

- Exported the RFM DataFrame and the final clustered data as **CSV** files for further exploration and use in business applications.
- Saved a visualization of the customer segments in a **PNG** file to provide a quick and easy reference for understanding the segmentation results.

---

## **Project Workflow**

1. **Data Loading**: Imported the dataset and performed an initial analysis to understand its structure and content.
2. **Data Cleaning**: Handled missing values and converted date columns to appropriate formats.
3. **Feature Engineering**: Calculated Recency, Frequency, and Monetary values for each customer, creating the foundation for RFM analysis.
4. **Data Scaling**: Scaled the RFM metrics to ensure fair contribution in clustering.
5. **Clustering**: Applied the K-Means algorithm, determined an optimal number of clusters, and grouped customers accordingly.
6. **Visualization**: Created an insightful scatter plot to represent the distribution of customer segments.
7. **File Export**: Saved both the clustered data and the visualization for further use in business applications.

---

## **Technologies and Libraries Used**

- **Python**: Core programming language for data processing and analysis.
- **Pandas**: Used for data manipulation and cleaning.
- **Matplotlib & Seaborn**: Used for data visualization and creating insightful charts.
- **Scikit-learn**: Utilized for scaling data and applying the K-Means Clustering algorithm.
- **Excel/CSV**: Data export formats for easy business use and further analysis.

---

## **Potential Use Cases**

1. **Customer Segmentation for Marketing**: Businesses can segment their customers based on Recency, Frequency, and Monetary value, enabling them to personalize their marketing efforts and improve customer retention.
2. **Targeted Campaigns**: By identifying high-value customers, businesses can focus their efforts on customer retention strategies, offering personalized promotions and discounts.
3. **Churn Prediction**: The Recency metric can be used to predict customer churn and implement re-engagement campaigns for customers who haven't made recent purchases.
4. **Product Recommendations**: Insights from the clusters can help in recommending specific products to different customer segments based on their purchasing behavior.

---

## **Challenges and Future Improvements**

- **Data Quality**: The success of RFM and clustering relies heavily on the quality of the data. In future iterations, we can include additional data points like customer demographics or product categories to further refine the segmentation.
- **Cluster Optimization**: While we used 4 clusters in this project, future work could involve experimenting with different cluster sizes or even applying other clustering algorithms such as **DBSCAN** or **Hierarchical Clustering**.
- **Dynamic Segmentation**: Implementing a real-time or dynamic segmentation process where customer clusters are updated as new data comes in can greatly improve the accuracy and usefulness of these insights.

---

## **Conclusion**

This project successfully demonstrates how **RFM analysis** combined with **K-Means Clustering** can be used to segment customers and provide actionable insights for business decision-making. By identifying distinct customer groups, businesses can optimize their marketing strategies, improve customer retention, and increase revenue. This project showcases a powerful data-driven approach to understanding customer behavior and tailoring efforts to meet their needs.

---

## **Next Steps**

- **Model Improvement**: Explore other clustering techniques to compare the performance and effectiveness in segmenting customers.
- **Real-time Integration**: Implement a dynamic dashboard for real-time customer segmentation insights.
- **Cross-Sell and Up-Sell Opportunities**: Analyze clusters to identify potential cross-sell and up-sell opportunities for specific customer segments.

---

## **How to Run the Project**

1. Clone the repository from GitHub.
2. Install the required Python libraries using:
   ```
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook or Python script to load the data and generate the RFM analysis and customer clusters.
4. Inspect the final CSV files and visualizations stored in the `output` folder.

---

## **Input and Output Information**

The input data must be stored in a CSV file named `data.csv`, located in the `./data/` directory. This CSV file should contain the following key columns:

- `CustomerID`: Unique identifier for each customer.
- `InvoiceNo`: Unique invoice number for each transaction.
- `InvoiceDate`: The date of the transaction.
- `Quantity`: The quantity of items purchased in the transaction.
- `UnitPrice`: The price per unit of the purchased item.

The output will be saved in the `./output/` folder, and it includes:

- `rfm_data.csv`: A CSV file containing the calculated **Recency, Frequency, and Monetary** values for each customer.
- `clustered_data.csv`: A CSV file with the final customer segments and cluster assignments.
- `customer_segments_plot.png`: A visual representation of the customer segments based on Recency and Monetary values.
- `customer_segments_output.csv`: The final file with all processed data and cluster information.

Make sure these columns are present in the input CSV for the script to run properly and generate the desired output.

---
