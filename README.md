# **Customer Segmentation App**

### **Overview**
This project is a customer segmentation tool built using a machine learning approach. It enables businesses to identify distinct customer groups based on their purchasing behavior. The app is built with Flask for local deployment and can help companies tailor marketing strategies, increase retention, and improve customer lifetime value.

### **Business Understanding**
The goal of this project is to help e-commerce or retail businesses:
- Understand different customer personas based on their behavior.
- Design personalized campaigns for each customer segment.
- Allocate marketing budget more effectively.

### **Dataset**
Source: UCI Machine Learning Repository (https://archive.ics.uci.edu/dataset/352/online+retail)

Name: Online Retail Dataset
Attributes:
- InvoiceNo, StockCode, Description, Quantity
- InvoiceDate, UnitPrice, CustomerID, Country

### **Data Understanding & Preprocessing**
1. Remove missing CustomerID: These rows can't be used for segmentation.
2. Feature Engineering:
- TotalPrice = Quantity * UnitPrice
- Recency: Days since the customer's last purchase
- Frequency: Number of unique invoices
- Monetary: Total spent
3. Log Transformation: Applied to Monetary and Frequency to reduce skewness
4. Scaling: StandardScaler used to normalize Recency, Frequency_log, and Monetary_log
