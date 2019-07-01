import matplotlib.pyplot as plt  
import numpy as np
import math
from sklearn.cluster import KMeans
import random, os

testMatrix = []
test_matrix = open("test_matrix_test_users_100_random_0.txt", "r")
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

	# Para cada ponto dentro do cluster alvo
	for j in range(0,len(target_cluster[0])):
		accounted = 0
		sum_i = 0
		for i in range(0,len(target_cluster)):
			if target_cluster[i][j] > 0:
				sum_i = sum_i + target_cluster[i][j]
				accounted = accounted + 1
			else:
				pass
		if accounted > 0:		
			average = sum_i / accounted
		else:
			average = 0

		if average > 0:
			rating_averages[j] = average
		else:
			rating_averages[j] = random.randint(1,5)


	# result = open("prediction_results.txt", "a+")

	# result.write("User ids and movies ids have to be mapped back to their original ids within the original dataset!\n\nRating predictions results: \n\n")

	count = 0	
	accounted = 0	
	# Guess rating when predicted equals 0
	for rate in rating_averages:
		if target_user_vector[count] != 0:
			content = "Movie id: " + str(count) + "-> Predicted rating: " + str(round(rate)) + "[" + str(target_user_vector[count]) + "]"
			# print(content)
			# result.write(content + "\n")
			if round(rate) == target_user_vector[count]:
				correct_count = correct_count + 1
			else:
				wrong_count = wrong_count + 1
			accounted = accounted + 1
		count = count + 1

	

	# averages_sum = averages_sum + average_correct_given
	# total_predictions_made = total_predictions_made + (correct_count + wrong_count)

	# print("Correct count: " + str(correct_count))
	# print("Wrong count: " + str(wrong_count))
	# print("Total count: " + str((correct_count + wrong_count)))
	print("[" + str(test_users_count) + "] predicted")

	# result.close()

average_correct_given = correct_count / (correct_count + wrong_count)

print("Test users count: " + str(test_users_count))
print("Total predictions made: " + str((correct_count + wrong_count)))
print("Average of correct answers: " + str(correct_count / (correct_count + wrong_count)))