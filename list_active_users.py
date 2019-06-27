#!/usr/bin/env python

import os

# Getting all files within target directory.
movies_files = os.listdir('training_set/')

# opening user file			
final_file = open("evaluations_per_user.txt","a+")

users_ratings_count = dict()

# Looping through each file found.
for movie_file in movies_files:
	# Open current traning file.
	movie_ratings = open('training_set/' + movie_file, "r")

	# Counting ratings for this movie
	movie_id_retrieved = 0
	for line in movie_ratings:
		if movie_id_retrieved == 0:
			movie_id_retrieved = 1
		else:
			key = line.split(',')[0] # user id

			if key in users_ratings_count:
				users_ratings_count[key] += 1
			else:
				users_ratings_count[key] = 1

	# Closing current movie file
	movie_ratings.close()

	print("> file '" + movie_file + "' finished parsing.")
# Saving to file
users_ratings_count_sorted = sorted(users_ratings_count.items(), key=lambda x:x[1], reverse=True)

for user in users_ratings_count_sorted:
	user_parsed = ((str(user).replace('(', '')).replace(')', '')).replace("'", '')
	final_file.write(user_parsed + "\n")

# closing final file
final_file.close()
	