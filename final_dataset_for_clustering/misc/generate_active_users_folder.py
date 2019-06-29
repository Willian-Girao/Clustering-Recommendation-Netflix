#!/usr/bin/env python

import os

# Creating folder to hold created files
if not os.path.exists('top_1k_active_users'):
	os.makedirs('top_1k_active_users')

# Top n active user
active_users = dict()
top_active_users_file = open('top_1k_active_users.txt', "r")
for user in top_active_users_file:
	user_id = user.replace('\n', '')

	if user_id not in active_users:
		active_users[user_id] = user_id

# Close file
top_active_users_file.close()

# Getting all files within target directory.
training_files = os.listdir('top_1k_rated_movies_2/')

# Looping through each file found.
count = 0
for file in training_files:
	# Open current traning file.
	current_file = open('top_1k_rated_movies_2/' + file, "r")

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

	# 'file_content' contains only information from file associated with active users - save them to theirs respective files	
	for key, value in file_content.items():
		# print("		- Saving user's '" + value['user_id'] + "' ratings...")
		# open user file
		target_folder = 'C:/Users/willi/UFF/Machine Learning/download/final_datasets_2/top_1k_active_users'
		user_file = open(os.path.join(target_folder, value['user_id'] + "_movies.txt"),"a+")
		user_file.write(movie_id + ", " + value['rating'] + "\n")
		user_file.close()		
		# wait = input("CONTENT SAVED")	

	print("> file '" + file + "' finished parsing.")
	count = count + 1
	print(str(count) + "/1000")