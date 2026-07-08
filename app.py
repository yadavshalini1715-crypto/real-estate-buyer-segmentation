import pandas as pd
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("buyer_data.csv")

# Display first 5 rows
print(data.head())

# Select features
x = data[['Age', 'Income']]

# Create K-Means model
model = KMeans(n_clusters=3, random_state=42)

# Train model
model.fit(x)

# Add cluster labels
data['Cluster'] = model.labels_

# Show result
print(data)
