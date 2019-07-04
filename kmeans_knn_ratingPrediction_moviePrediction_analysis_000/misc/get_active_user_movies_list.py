#!/usr/bin/env python

import os
import helper

# Creating folder to hold created files
if not os.path.exists('movies_per_user'):
	os.makedirs('movies_per_user')

# Top n active user
active_users = dict()
top_active_users_file = open('top_5_least_active_users.txt', "r")
for user in top_active_users_file:
	user_id = user.replace('\n', '')

	if user_id not in active_users:
		active_users[user_id] = user_id

# Close file
top_active_users_file.close()

# Getting all files within target directory.
training_files = os.listdir('training_set/')

# Looping through each file found.
for file in training_files:
	# Open current traning file.
	current_file = open('training_set/' + file, "r")

	is_first_line = True
	movie_id = ""
	file_content = dict()
	for line in current_file:
		if is_first_line:
			movie_id = (line.replace('\n', '')).replace(':', '')
			is_first_line = False
		else:
			parsed_line = (line.replace('\n', '')).split(',')
			user_id = parsed_line[0]
			user_rating = parsed_line[1]

			# Check if I want this info
			if user_id in active_users:
				file_content[user_id] = {'user_id': user_id, 'rating': user_rating}	
	# closing file
	current_file.close()
	print("> file '" + file + "' finished parsing.")

	# 'file_content' contains only information from file associated with active users - save them to theirs respective files	
	for key, value in file_content.items():
		print("		- Saving user's '" + value['user_id'] + "' ratings...")
		# open user file
		target_folder = 'C:/Users/willi/UFF/Machine Learning/download/movies_per_user'
		user_file = open(os.path.join(target_folder, value['user_id'] + "_movies.txt"),"a+")
		user_file.write(movie_id + ", " + value['rating'] + "\n")
		user_file.close()
		# wait = input("CONTENT SAVED")	