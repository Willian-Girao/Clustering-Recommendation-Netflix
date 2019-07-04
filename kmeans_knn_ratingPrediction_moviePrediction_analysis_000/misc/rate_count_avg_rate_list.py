#!/usr/bin/env python

import os
import csv

# Getting all files within target directory.
movies_files = os.listdir('training_set/')

# opening user file			
final_file = open("movies_rateCount_avgRate_class_totalDataset.txt","a+")

# List with rating to be sorted
ratings_array = []

# Looping through each file found.
for movie_file in movies_files:
	# Open current traning file.
	movie_ratings = open('training_set/' + movie_file, "r")

	# Counting ratings for this movie
	ratings_count = 0
	content = ""
	movie_id = ""
	movie_id_retrieved = 0
	avg_rate = 0
	for line in movie_ratings:
		# Summing rates to calculate average
		if movie_id_retrieved == 1:
			avg_rate += int(line.split(',')[1])

		# Getting movie id from file
		if movie_id_retrieved == 0:
			movie_id = line.replace(':', '')
			movie_id = movie_id.replace('\n','')
			movie_id_retrieved = 1

		ratings_count += 1

	# removing movie_id that was accounted 
	ratings_count -= 1

	# Calculating avg rate
	avg = avg_rate / ratings_count

	# Checking class
	movie_quality_label = "ruim"

	if avg < 1.66:
		movie_quality_label = "ruim"
	elif avg > 1.66 and avg < 3.32:
		movie_quality_label = "medio"
	elif avg > 3.32:
		movie_quality_label = "bom"

	# Saving movie id and rating count to array	
	ratings_array.append([str(movie_id), int(ratings_count), str(round(avg,2)), str(movie_quality_label)])

	# Closing current movie file
	movie_ratings.close()

	print("> file '" + movie_file + "' finished parsing.")
# Sorting array with rating
ratings_array.sort(key=lambda x:x[1], reverse=True)

# Saving to file
for data in ratings_array:
	if data[1] > 90.000:
		final_file.write(str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + "\n")

# closing final file
final_file.close()
	