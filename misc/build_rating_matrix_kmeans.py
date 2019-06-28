#!/usr/bin/env python

import os

# Getting all files within target directory.
movies_files = os.listdir('top_1k_active_users_movies/')

# Target user id
target = '1054884'

# opening user file			
target_user_ratings = open('top_5_least_active_users/' + target + '_movies.txt', "r")

final_file = open('Ui_TRAINING_' + target + '_rated_movies.txt', "a+")

target_rated_moviesIds = []
for line in target_user_ratings:
	movie_id = line.split(',')[0]
	target_rated_moviesIds.append(movie_id)

for file in movies_files:
	user_id = file.split('_')[0]
	if user_id != target:
		training_file = open('top_1k_active_users_movies/' + file, "r")	

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
		final_file.write(content_aux[:-1] + '\n')

		print("> Finished parsing file '" + file + "' - rated count: " + str(found_training_id_count))
			
