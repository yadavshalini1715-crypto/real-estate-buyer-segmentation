import pandas as pd 
from sklearn.cluster import KMeans
#load dataset 
data=pd.read_csv("buyer_data.csv")
# Display first 5 rows
print(data.head())
# Select features 
x= data[['age','income']]
# Create K-Means model 
model = KMeans (n_clusters=3, randaom_state=42)
model.fit(x)
#Add cluster labels
data ['cluster']= model.labels_
#show result
print(data)
