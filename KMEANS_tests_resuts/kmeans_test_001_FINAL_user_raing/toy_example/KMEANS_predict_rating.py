import matplotlib.pyplot as plt  
import numpy as np
import math
from sklearn.cluster import KMeans

# Wanted n closest neighbors
n_closest_to_target = 2

# Contain vector representing target user ratings
target_user_vector = []
# Saving point to cluster afterwards
user_to_predict = open('toy_test.txt', 'r')
for single_line in user_to_predict:
	raw = single_line.split(',')
	for rating in raw:
		target_user_vector.append(int(rating))

# Array with actual predictions for the last movie
real_original_ratings = []

# Matrix R of points
matrix_R = []

# Opening file containing user_ratings.
datapoint_file = open('toy_training.txt', 'r')

# Populating matrix R with datapoints
count_rows = 0
for line in datapoint_file:
	matrix_row_i = []

	raw = line.split(',')

	count = 0
	for rating in raw:
		matrix_row_i.append(int(rating))
		count = count + 1
	count_rows = count_rows + 1
	print("Row " + str(count_rows) + " added - entries: " + str(count))
	
	matrix_R.append(matrix_row_i)	

X = np.array(matrix_R)

kmeans = KMeans(n_clusters=2)
kmeans.fit(X) # Clusters crated

cluster_prediction = kmeans.predict([target_user_vector])[0]

print('\nTarget belongs to cluster: ' + str(cluster_prediction) + ".\n")

# Getting points within target cluster
target_cluster = []
for point in np.where(kmeans.labels_ == cluster_prediction)[0]:
		target_cluster.append(X[point])
print("\n")

# print("Points in target cluster: ")
# for point in target_cluster:
# 	print(point)

rating_averages = []
for x in range(0,len(target_user_vector)):
	rating_averages.append(0)

for point_within_cluster in target_cluster:
	rating_averages_index = 0
	for rating in point_within_cluster:
		rating_averages[rating_averages_index] = rating_averages[rating_averages_index] + int(rating)
		rating_averages_index = rating_averages_index + 1

for x in range(0, len(rating_averages)):
	rating_averages[x] = rating_averages[x] / n_closest_to_target


count = 0
for rate in rating_averages:
	print("Movie id: " + str(count) + "-> Predicted rating: " + str(rate))
	count = count + 1