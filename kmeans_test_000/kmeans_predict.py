import matplotlib.pyplot as plt  
import numpy as np
import math
from sklearn.cluster import KMeans

# Target user id
target_user_id = '2611141'

def calcDistance(point_a, point_b):
	comp_sum = 0
	for x in range(0,len(point_a)):
		comp_sum = comp_sum + (point_a[x] - point_b[x])**2
	return math.sqrt(comp_sum)

def predictRate(targe_user, top_n_closest, X, real_original_ratings):
	print('Closest points:')
	wanted_indexes = []
	for close_point in top_n_closest:
		X_datapoint_index = 0
		for datapoint in X:
			if np.array_equal(close_point['datapoint'], datapoint):
				wanted_indexes.append(X_datapoint_index)
				print(list(close_point['datapoint']))
			X_datapoint_index = X_datapoint_index + 1
	print('Target point:')
	print(list(targe_user))
	print('\n')

	sum_rates = 0
	for index in wanted_indexes:
		sum_rates = sum_rates + real_original_ratings[index]

	return sum_rates / len(wanted_indexes)

# Wanted n closest neighbors
n_closest = 10

# Opening file containing user_ratings (taret user is the first row).
datapoint_file = open(target_user_id + '_R_Matrix_TRAINING_rated_movies.txt', 'r')

# Contain vector representing target user ratings
target_user_vector = []

# Array with actual predictions for the last movie
real_original_ratings = []

# Matrix R of points
matrix_R = []

# Populating matrix R with datapoints
targe_user_not_retrieved = True
for line in datapoint_file:
	matrix_row_i = []

	# Saving target user vector
	if targe_user_not_retrieved:
		for item in line.split(',')[:-1]:
			target_user_vector.append(int(item))			
		targe_user_not_retrieved = False

	real_original_ratings.append(int(line.split(',')[-1].replace('\n', '')))		

	for item in line.split(',')[:-1]:
			matrix_row_i.append(int(item))
	matrix_R.append(matrix_row_i)	

X = np.array(matrix_R)

# np.random.shuffle(X)

# for row in X:
# 	print(row)
# pause = input('PAUSED.')

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)


cluster_label = 0
targe_centroids_distances = []
for centroind in kmeans.cluster_centers_:
	distance = calcDistance(target_user_vector, centroind)
	targe_centroids_distances.append({'distance': distance, 'cluster_label': cluster_label})
	cluster_label = cluster_label + 1

sorted_target_clusters = sorted(targe_centroids_distances, key = lambda i: i['distance']) 
for dist in sorted_target_clusters:
	print(str(dist))

print('\nTarget belongs to cluster: ' + str(sorted_target_clusters[0]['cluster_label']) + " - Distance: " + str(sorted_target_clusters[0]['distance']))


# Getting points within target cluster
target_cluster = []
for point in np.where(kmeans.labels_ == sorted_target_clusters[0]['cluster_label'])[0]:
		target_cluster.append(X[point])
print("\n")


target_vec_aux = np.array(target_user_vector)

calculated_distances = []
for datapoint in target_cluster:
	distance = calcDistance(target_vec_aux, datapoint)
	calculated_distances.append({'distance': distance, 'datapoint': datapoint})


sorted_distances = sorted(calculated_distances, key = lambda i: i['distance'])

count = 0
top_n_closest = []
for dist in sorted_distances:
	if dist['distance'] != 0.0:
		if count < n_closest:
			top_n_closest.append(dist)
		else:
			break
		count = count + 1

for closest in top_n_closest:
	print(closest['distance'])

print('\n')

prediction = predictRate(target_vec_aux, top_n_closest, X, real_original_ratings)

final_results = open("predictions_results.txt", "a+")

print("\n=== PREDICTION ===\n")
print("Predicted: " + str(prediction) + "\n")
print("Actual: " + str(real_original_ratings[0]) + "\n")

final_results.write("User id: " + target_user_id + " - " + "Predicted: " + str(prediction) + " - " + "Actual: " + str(real_original_ratings[0]) + "\n")
final_results.close()

