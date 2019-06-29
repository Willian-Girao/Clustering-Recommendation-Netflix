#!/usr/bin/env python

import os, shutil

# Creating folder to hold created files
if not os.path.exists('top_1k_rated_movies'):
	os.makedirs('top_1k_rated_movies')

# Top n rated movies
top_rated_movies = open('top_1k_rated_movies.txt', "r")

# Getting wanted files names
wanted_movies_names_files = []
for movie_info in top_rated_movies:
	movie_id = int(movie_info.split(',')[0])

	name_start = "mv_"
	for x in range(0,(7 - len(str(movie_id)))):
		name_start += "0"
	name_start += str(movie_id) + ".txt"
	wanted_movies_names_files.append(name_start)

# Movies in current folder
training_files = os.listdir('./')

# Moving to destination target
count = 0
for f in wanted_movies_names_files:
    shutil.move(f, 'top_1k_rated_movies')
    count = count + 1
    print("> Moved file '" + str(count) + "'.")
    



