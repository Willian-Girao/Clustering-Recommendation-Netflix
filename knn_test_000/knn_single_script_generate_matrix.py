#!/usr/bin/env python

import os

# [ GENERATING TARGET USER ROW ]

# Target user id
# target_user_id = '1054884'
# target_user_id = '1081982'
# target_user_id = '1512089'
# target_user_id = '2151955'
target_user_id = '2611141'

# Target test folder
target_test_folder = 'test_dataset/'
target_training_folder = 'training_dataset/'

# opening user file			
target_user_ratings = open(target_test_folder + target_user_id + '_movies.txt', "r")
single_target_user_file = open('target_userId_' + target_user_id + '_rated_movies.txt', "a+")

target_user_row_content = ""
line_count = 0
for line in target_user_ratings:
	line_count = line_count + 1
	content = line.split(',')
	rate = content[1].replace('\n', '')
	target_user_row_content += rate.replace(' ', '') + ', '

print('Number of movies rated: ' + str(line_count))

target_user_row_content_aux = target_user_row_content[:-1]
single_target_user_file.write(target_user_row_content_aux[:-1])

# closing final file
single_target_user_file.close()


# [ RETREAVING TRAINING POINTS AS ROWS ]

# opening user file			
target_user_ratings = open(target_test_folder + target_user_id + '_movies.txt', "r")

# Getting all files within training directory
movies_files = os.listdir(target_training_folder)

training_points_Ui = open(target_user_id + '_R_Matrix_TRAINING_rated_movies.txt', "a+")

training_points_Ui.write(target_user_row_content_aux[:-1] + '\n')

target_rated_moviesIds = []
for line in target_user_ratings:
	movie_id = line.split(',')[0]
	target_rated_moviesIds.append(movie_id)

for file in movies_files:
	user_id = file.split('_')[0]
	if user_id != target_user_id:
		training_file = open('training_dataset/' + file, "r")	

		current_user_rated_moviesIds = []
		curr_trainin_file_ratings = dict()
		found_training_id_count = 0

		for line in training_file:
			movie_id = line.split(',')[0].replace('\n', '')
			movie_rate = line.split(',')[1].replace('\n', '')
			curr_trainin_file_ratings[movie_id] = movie_rate.replace(' ', '')

		training_file.close()

		content = ""
		for target_mids in target_rated_moviesIds:
			if target_mids in curr_trainin_file_ratings:
				content += curr_trainin_file_ratings[target_mids] + ", "				
			else:
				content += "0, "
			found_training_id_count = found_training_id_count + 1

		if found_training_id_count < len(target_rated_moviesIds):
			paused = input('SHOULD NOT HAVE ENTERED HERE')
			for x in range(0,(len(target_rated_moviesIds) - found_training_id_count)):
				content += "0, "
				found_training_id_count = found_training_id_count + 1				

		content.replace('\n', '')
		content_aux = content[:-1]

		aux_2 = content_aux[:-1]

		if aux_2[-1] != '0':
			training_points_Ui.write(content_aux[:-1] + '\n')
		print("> Finished parsing file '" + file + "' - rated count: " + str(found_training_id_count))
training_points_Ui.close()