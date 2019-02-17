# 1976 Vehicle Data and K Means
This project is the the first data set where I used my kmeans algorithm to cluster data and find centroids of data.
We picked the auto-mpg data set from kaggle to use my algorithm on.
We picked the y-axis to be mpg and the x-axis to be weight of vehicles.  I used different colors to cluster the amount of cylinders each car had.  The vehicle data is from the year 1976, avoiding multiple years and problems of time series analysis.
Go into terminal and run command python3 cluster_cylinders.py
You will see four different boxes pop up.  The top two boxes are the data points plotted,  one with cylinders in color and the other with non-colored data.  This gives you an opportunity to see the data points plotted.
The bottom two graphs show the kmeans algorithm vs the actual known cylinders.  

# How the kmeans algorithm works:
So first we initialize the kmeans class with our training data and the number of clusters we want.
Then we randomize the number of data points and use the first number of points to randomly place our centroids.
We then iterate through every data point and calculate the distance for every centroid.  we then pick the minimum distance and determine the nearest centroid and store that into an array.
We then go through the associated data points to each centroid and calculate the total mean for those data points,  then we are able to place the centroid based on that calculation.
We then interate through this process a certain amount of times to achieve the minimum distance for our clusters and their associated data points.

# K-means optimization
The optimization of the K-means algorithm focuses on the "elbow" method and uses the Calinski & Harabasz criteria to choose the optimal number of K clusters for K-means algorithm. All data sets have a  sum of squares of each point from the cluster means. With K = 1, the mean is just the total sum of squares which forms the comparison basis for the elbow method. As more clusters are added the sum of squares decreases and exponentially approaches zero. The optimizer starts at K = 2 and increases K until the sum of squares relative to the total sum of squares approaches a ratio less than 1 and close to zero (default is 0.0001). After this value is reached, we can evaluate the K's with the Calinski & Harabasz criteria to select the one with the maximum score which indicates the optimal number of clustering.

# How the data was organized:
We used vehicle dataset,  we then used pandas to manipulate the data set.  We used mpg, weight and cylinders from the model year 1976. All regressors were normalized to the range of [-1, 1] to avoid the problem of weight dominating the algorithm. After the optimal K-means algorithm we denormalize the clusters to fit in the original data set.
We used matplot lib to visualize the data and any clusters that appeared.

# Conclusion:
As you can see, there is correlation between mpg, weight, and cylinders.  The higher mpg and less weight typically means less cylinders.  The kmeans algorithm does not perfecly cluster to just 3 clusters we had suspected but it does a very good job. Generally there is little overlap between cylinder groups and clusters are generally proper or improper subsets of the cylinder groups, i.e. there might be multiple clusters of a cylinder type but no cluster that is comprised of half 4 and half 6 cylinder cars.

# External References:
1) Calinski & Harabasz: http://ethen8181.github.io/machine-learning/clustering_old/clustering/clustering.html
2) Elbow method: https://en.wikipedia.org/wiki/Elbow_method_(clustering)
