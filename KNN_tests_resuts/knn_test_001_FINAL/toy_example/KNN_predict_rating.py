import matplotlib.pyplot as plt  
import numpy as np
import math
from sklearn.neighbors import KNeighborsClassifier

def calcDistance(point_a, point_b):
	comp_sum = 0
	for x in range(0,len(point_a)):
		comp_sum = comp_sum + (point_a[x] - point_b[x])**2
	return math.sqrt(comp_sum)

# Wanted n closest neighbors
n_closest_to_target = 0

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
target_last_movie_ratings_as_label = []
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
	target_last_movie_ratings_as_label.append(matrix_row_i[-1])

# print(target_last_movie_ratings_as_label)

X = np.array(matrix_R)
Y = np.array(target_last_movie_ratings_as_label)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, Y)


final = []
aux = []
for x in target_user_vector:
	aux.append(x)
final.append(aux)
print(final)
cluster_prediction = knn.predict(final)[0]

print('\nTarget belongs to cluster: ' + str(cluster_prediction) + ".\n")

if cluster_prediction == 0:
	cluster_prediction = random.randint(1,5)

if cluster_prediction == target_user_vector[-1]:
	pass