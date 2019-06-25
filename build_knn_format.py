#!/usr/bin/env python

import os
import csv
import helper

# Getting all files within target directory.
training_parsed = os.listdir('user_movies_rated/')

# opening user file			
final_file = open("knn_data_csv.csv","a+")

sorted_training_files = []
for filename in training_parsed:
	sorted_training_files.append(filename)

sorted_training_files.sort(key=lambda x:int(helper.last_4chars(x)))

# Looping through each file found.
for file in sorted_training_files:
	# Open current traning file.
	costumer_ratings_file = open('user_movies_rated/' + file, "r")

	last_movie_id = -1
	user_id_added = 0
	for movie_i in costumer_ratings_file:
		content = ""
		splited_line = movie_i.split(',')

		user_id = splited_line[0]
		movie_id = splited_line[1]
		user_rating = splited_line[2]
		rating_date = splited_line[3]

		if user_id_added == 0:
			content = str(user_id)
			user_id_added = 1	

		if (last_movie_id == -1):
			last_movie_id = 0

		gap = int(movie_id) - int(last_movie_id)

		# completing missing ratings
		if gap > 1:
			for x in range(1, gap):
				content += ";0"		

		content += ";" + str(user_rating)

		# adding actually existing rating value
		final_file.write(content)

		# saving last movie id
		last_movie_id = int(movie_id)

	# completing missing movie ids
	if last_movie_id != 30:
			for x in range(last_movie_id+1, 31):
					final_file.write(";0")

	final_file.write("\n")
	# closing file
	costumer_ratings_file.close()
	print("> file '" + file + "' finished parsing.")
# closing final file
final_file.close()
	