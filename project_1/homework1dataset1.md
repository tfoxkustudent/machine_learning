# 1976 Vehicle Data and K Means
This project is the the first data set where I used my kmeans algorithm to cluster data and find centroids of data.
We picked the auto-mpg data set from kaggle to use my algorithm on.
We picked the y-axis to be mpg and the x-axis to be weight of vehicles.  I used different colors to cluster the amount of cylinders each car had.  The vehicle data is from the year 1976.
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
The way to optimize K-means is to optimize the number of clusters selected. Each data set has a total sum of squares (TSS) of vector norms from the data set's mean. As clusters are used, the residual sum of squares (RSS) of the subsets norms from the cluster mean can be used to judge a convergence limit. This technique is based on the "elbow" method as described in an external reference. The algorithm keeps adding to K until the RSS/TSS reaches a lower threshold. At this point the algorithm evaluates each K's Calinski-Harabasz index to determine the optimal K which occurs at the maximum Calinski-Harabasz score. Since the Calinski-Harabasz index seeks to minimize the amount of clusters as well as RSS of the data, this seeks a good middle ground for determining the optimal number of clusters. 

# How the data was organized:
We used vehicle dataset,  we then used pandas to manipulate the data set.  We used mpg, weight and cylinders.  We also used model year 1976.
We used matplot lib to visualize the data.

# Conclusion:
As you can see, there is correlation between mpg, weight, and cylinders.  The higher mpg and less weight typically means less cylinders.  The kmeans algorithm does not cluster the data exactly the same but it does a very good job.  We have developed an algorithm to automatically cluster the data.  This could have possible benefits in the future,  such as determining the optimal number of cylinders for a vehicle.  Our k means algorithm could be extremely beneficial in feature learning moving forward.
