#!/usr/bin/env python

# Script maps from final training user's id to original dataset user's id

final_file = open("mapped_movies_ids.txt", "a+")

movies_list = open("top_1k500_rated_movies.txt", "r")

id_counter = 1

for line in movies_list:
	movie_id = line.split(',')[0]
	final_file.write(movie_id + ", " + str(id_counter) + "\n") 	
	print(movie_id + " => " + str(id_counter))
	id_counter = id_counter + 1

final_file.close()
movies_list.close()

