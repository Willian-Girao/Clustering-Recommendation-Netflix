import matplotlib.pyplot as plt  
import numpy as np
import math
from sklearn.neighbors import KNeighborsClassifier
import random, os

def calcDistance(point_a, point_b):
	comp_sum = 0
	for x in range(0,len(point_a)):
		comp_sum = comp_sum + (point_a[x] - point_b[x])**2
	return math.sqrt(comp_sum)

testMatrix = []
test_matrix = open("test_matrix_test_users_100_random_1.txt", "r")
for line in test_matrix:
	row_i = line.split(',')
	row = []
	count = 0
	for rating in row_i:
		row.append(int(rating))
		count = count + 1
	testMatrix.append(row)

# test_users = os.listdir('users_to_predict/')

test_users_count = 0
averages_sum = 0
total_predictions_made = 0

correct_count = 0
wrong_count = 0
for userr in testMatrix:	
	# User to be clustered
	# test_file = 'user_615032_ratings_forTop1k500Movies.txt'
	# test_file = file
	test_users_count = test_users_count + 1

	# Datapoints to generate clusters
	training_file = 'userId_X_movieId_ratings_matrix.txt'

	# Wanted n closest neighbors
	n_closest_to_target = 10

	# Contain vector representing target user ratings
	target_user_vector = userr
	# Saving point to cluster afterwards
	# user_to_predict = open('users_to_predict/' + test_file, 'r')
	# for single_line in user_to_predict:
	# 	raw = single_line.split(',')
	# 	for rating in raw:
	# 		target_user_vector.append(int(rating))

	# Array with actual predictions for the last movie
	real_original_ratings = []

	# Matrix R of points
	matrix_R = []

	# Opening file containing user_ratings.
	datapoint_file = open(training_file, 'r')

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
		# print("Row " + str(count_rows) + " added - entries: " + str(count))
		
		matrix_R.append(matrix_row_i)	
		target_last_movie_ratings_as_label.append(matrix_row_i[-1])

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
		correct_count = correct_count + 1
	else:
		wrong_count = wrong_count + 1


	# result.close()

average_correct_given = correct_count / (correct_count + wrong_count)

print("Test users count: " + str(test_users_count))
print("Total predictions made: " + str((correct_count + wrong_count)))
print("Average of correct answers: " + str(correct_count / (correct_count + wrong_count)))