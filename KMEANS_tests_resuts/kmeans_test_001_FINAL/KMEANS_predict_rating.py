import matplotlib.pyplot as plt  
import numpy as np
import math
from sklearn.cluster import KMeans

# User to be clustered
test_file = 'user_615032_ratings_forTop1k500Movies.txt'

# Datapoints to generate clusters
training_file = 'userId_X_movieId_ratings_matrix.txt'

# Wanted n closest neighbors
n_closest_to_target = 10

# Contain vector representing target user ratings
target_user_vector = []
# Saving point to cluster afterwards
user_to_predict = open(test_file, 'r')
for single_line in user_to_predict:
	raw = single_line.split(',')
	for rating in raw:
		target_user_vector.append(int(rating))

# Array with actual predictions for the last movie
real_original_ratings = []

# Matrix R of points
matrix_R = []

# Opening file containing user_ratings.
datapoint_file = open(training_file, 'r')

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
	# print("Row " + str(count_rows) + " added - entries: " + str(count))
	
	matrix_R.append(matrix_row_i)	

X = np.array(matrix_R)

kmeans = KMeans(n_clusters=2)
# Clustering
kmeans.fit(X) 

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

points_account = 0
for point_within_cluster in target_cluster:
	if points_account < n_closest_to_target:		
		rating_averages_index = 0
		for rating in point_within_cluster:
			rating_averages[rating_averages_index] = rating_averages[rating_averages_index] + int(rating)
			rating_averages_index = rating_averages_index + 1
		points_account = points_account + 1
	else:
		break

for x in range(0, len(rating_averages)):
	rating_averages[x] = rating_averages[x] / n_closest_to_target


result = open("prediction_results.txt", "a+")

result.write("User ids and movies ids have to be mapped back to their original ids within the original dataset!\n\nRating predictions results: \n\n")

count = 0
for rate in rating_averages:
	content = "Movie id: " + str(count) + "-> Predicted rating: " + str(rate)
	# print(content)
	result.write(content + "\n")
	count = count + 1

result.close()