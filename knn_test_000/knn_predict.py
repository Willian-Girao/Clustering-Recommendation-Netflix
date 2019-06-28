import matplotlib.pyplot as plt  
import numpy as np
import math
from sklearn.neighbors import KNeighborsClassifier

# Target user id
# target_user_id = '1054884'
# target_user_id = '1081982'
# target_user_id = '1512089'
# target_user_id = '2151955'
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

	print('Closest ratings:')	
	sum_rates = 0
	for index in wanted_indexes:
		sum_rates = sum_rates + real_original_ratings[index]
		print(real_original_ratings[index])
	print('\n')

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

X = np.array(matrix_R) # Datapoints
Y = np.array(real_original_ratings) # Target

# np.random.shuffle(X)

# for row in X:
# 	print(row)
# pause = input('PAUSED.')

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, Y)

target_vec_aux = np.array(target_user_vector)

prediction = knn.predict([target_vec_aux])

final_results = open("knn_predictions_results.txt", "a+")

print("\n=== PREDICTION ===\n")
print("Predicted: " + str(prediction) + "\n")
print("Actual: " + str(real_original_ratings[0]) + "\n")

final_results.write("User id: " + target_user_id + " - " + "Predicted: " + str(prediction) + " - " + "Actual: " + str(real_original_ratings[0]) + "\n")
final_results.close()

