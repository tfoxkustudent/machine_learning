import pandas as pd
import matplotlib.pyplot as plt
from kmeans import k_means

#import CSV File
data = pd.read_csv('sensor_readings_2.csv', names=["First Reading","Second Reading", "Robot Move"])



# The data property that will be clustered
robot_moves = ["Slight-Right-Turn", "Sharp-Right-Turn", "Move-Forward", "Slight-Left-Turn"]

# The two data properties that will be tested
x_axis = 'First Reading'
y_axis = 'Second Reading'

#create a larger window to display four plots
plt.figure(figsize=(16,8))
#organize the four plots as subplots to fit in the window
plt.subplot(2,2,1)

#plot data mpg as x axis, weight as y axis, and label with cylinders
for robot_move in robot_moves:
    plt.scatter(
        data[x_axis][data['Robot Move'] == robot_move],
        data[y_axis][data['Robot Move'] == robot_move],
        label=robot_move
    )

#create x,y labels and titel and legend for cylinders
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.title('Initial Data')
plt.legend()

#plot data with no labels for reference
plt.subplot(2,2,2)
plt.scatter(
    data[x_axis][:],
    data[y_axis][:],
)
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.title('Initial Data(No Labels)')




# Total number of data points
n_data = data.shape[0]

# Get features.
train_data = data[[x_axis, y_axis]].values.reshape((n_data, 2))

# Enter k_means inputs.
clusters = 4  # Number of clusters into which we want to split our training dataset.
iterations = 50  # maximum number of training iterations.


# Init k_means instance.
k_means = k_means(train_data, clusters)

# Train k_means instance.
(centroids, nearest_centroid) = k_means.train(iterations)

# Plot actual clusters for reference
plt.subplot(2,2,3)
for robot_move in robot_moves:
    plt.scatter(
        data[x_axis][data['Robot Move'] == robot_move],
        data[y_axis][data['Robot Move'] == robot_move],
        label=robot_move
    )

plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.title('Actual Clusters')
plt.legend()

# Plot labeled cluster data
plt.subplot(2,2,4)
for centroid_id, centroid in enumerate(centroids):
    current_examples_indices = (nearest_centroid == centroid_id).flatten()
    plt.scatter(
        data[x_axis][current_examples_indices],
        data[y_axis][current_examples_indices],
        label='Cluster #' + str(centroid_id)
    )

# Plot the k-mean clusters.
for centroid_id, centroid in enumerate(centroids):
    plt.scatter(centroid[0], centroid[1], c='black', marker='x')

plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.title('K-Means Clusters')
plt.legend()

#organize subplots to not blend together
plt.tight_layout()
# Show all subplots.
plt.show()


