#!/usr/bin/env python

import os
import helper

# Creating folder to hold created files.
if not os.path.exists('user_movies_rated'):
	os.makedirs('user_movies_rated')

# Getting all files within target directory.
training_files = os.listdir('training_set/')

# Looping through each file found.
for file in training_files:
	# Open current traning file.
	current_file = open('training_set/' + file, "r")
	movie_id = 1 # Variable to hold current movie id.

	for line in current_file:
		# Check what type of line it is.
		line_type = helper.returnLineType(line)

		# Decide what to do with line.
		if line_type == 0:
			# saving movie id
			movie_id = line.split(':')[0]
		elif line_type == 1:
			# oppening file to insert new movie id

			# separating string
			parse = line.split(',')

			# getting userId, rating and date from line						
			user_id = parse[0]
			user_raing = parse[1]
			rating_date = parse[2]

			# opening user file			
			target_folder = 'C:/Users/willi/UFF/Machine Learning/dataset_preprocessing/user_movies_rated'
			user_file = open(os.path.join(target_folder, str(user_id) + "_movies.txt"),"a+")

			# =========================================================================================================
			# # checking if last movieId-1 has an entry for this file before saving new entry
			# user_file_aux = open(os.path.join(target_folder, str(user_id) + "_movies.txt"),"r")
			# last_saved_movie_id = "0"
			# for curr_file_line in user_file_aux:
			# 	last_saved_movie_id = curr_file_line.split(',')[1]

			# gap = int(movie_id) - int(last_saved_movie_id)
			# user_file_aux.close()

			# user_file_aux = open(os.path.join(target_folder, str(user_id) + "_movies.txt"),"a+")
			# # completing ids of movies not rated
			# for x in range(1,int(movie_id)): # 'x' goes from 1 to movie_id-1
			# 	content_fix = str(user_id) + "," + str((int(last_saved_movie_id) + x)) + "," + "0" + "," + "0000-00-00" + "\n"
			# 	user_file_aux.write(content_fix)
			# user_file_aux.close()	
			# =========================================================================================================

			# creating line content: USER_ID, MOVIE_ID, RATING, DATE
			content = str(user_id) + "," + str(movie_id) + "," + str(user_raing) + "," + str(rating_date)			

			# saving content to user file
			user_file.write(content)

			# closing file
			user_file.close()
			# wait = input("CONTENT SAVED")
	# closing file
	current_file.close()
	print("> file '" + file + "' finished parsing.")
	