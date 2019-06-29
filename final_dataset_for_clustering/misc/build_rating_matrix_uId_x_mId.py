#!/usr/bin/env python

import os

# Getting all files within target directory.
movies_files = os.listdir('top_1k_active_users/')

movies_ids_list = []
movies_ids_file = open("top_2k_rated_movies.txt", "r")
for movie_id in movies_ids_file:
	parsed = movie_id.split(',')[0]
	movies_ids_list.append(int(parsed))
movies_ids_list.sort()

print("\n> Total 2k top ids retrieved: " + str(len(movies_ids_list)))

final_file = open('userId_X_movieId_ratings_matrix.txt', "a+")

for file in movies_files:
	training_file = open('top_1k_active_users/' + file, "r")

	accounted = 0
	content = ""

	for entry in training_file:
		movie_id = entry.split(',')[0]
		rating = entry.split(',')[1].replace('\n', '')	

		if int(movie_id) in movies_ids_list:
			content += rating.replace(' ', '') + ", "
			accounted = accounted + 1
	training_file.close()
	
	left = 0
	for x in range(0,(len(movies_ids_list) - accounted)):
		content += "0, "
		accounted = accounted + 1
		left = left + 1

	print(file)
	print("Accounted: " + str(accounted) + "/2000")
	print("Left: " + str(left))
	pause = input('a')

	final_file.write(content[:-2] + "\n")

final_file.close()





			
