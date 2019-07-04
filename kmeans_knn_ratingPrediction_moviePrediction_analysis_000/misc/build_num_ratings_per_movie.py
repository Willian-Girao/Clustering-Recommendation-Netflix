#!/usr/bin/env python

import os
import csv

# Getting all files within target directory.
movies_files = os.listdir('training_set/')

# opening user file			
final_file = open("movies_rateCount.txt","a+")

# List with rating to be sorted
ratings_array = []

# Looping through each file found.
for movie_file in movies_files:
	# Open current traning file.
	movie_ratings = open('training_set/' + movie_file, "r")

	# Counting ratings for this movie
	ratings_count = 0
	movie_id = ""
	movie_id_retrieved = 0
	for line in movie_ratings:
		if movie_id_retrieved == 0:
			movie_id = line.replace(':', '')
			movie_id = movie_id.replace('\n','')
			movie_id_retrieved = 1
		ratings_count += 1

	# removing movie_id that was accounted 
	ratings_count -= 1

	# Saving movie id and rating count to array	
	ratings_array.append([str(movie_id), int(ratings_count)])

	# Closing current movie file
	movie_ratings.close()

	print("> file '" + movie_file + "' finished parsing.")
# Sorting array with rating
ratings_array.sort(key=lambda x:x[1], reverse=True)

# Saving to file
for data in ratings_array:	
	final_file.write(str(data[0]) + "	" + str(data[1]) + "\n")

# closing final file
final_file.close()
	