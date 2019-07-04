#!/usr/bin/env python

import os

movies_ids_list = []
movies_ids_file = open("top_1k500_rated_movies.txt", "r")
for movie_id in movies_ids_file:
	parsed = movie_id.split(',')[0]
	movies_ids_list.append(int(parsed))
movies_ids_list.sort()

print("\n> Total 1k500 top movie ids retrieved: " + str(len(movies_ids_list)))


# Final matrix file
matrix_file = open('testUsers_serId_X_movieId_ratings_matrix.txt', "a+")

# Getting all files within target directory.
users_files = os.listdir('test_users_for_prediction/')

# Sorting users ids in order to get correct mapping
user_ids_sorted = []
for file in users_files:
	user_ids_sorted.append(int(file.replace('_movies.txt', '')))

# User ids in ascending order
user_ids_sorted.sort()


total_left = 0
for user_id in user_ids_sorted:
	# Open user file - getting user ratings
	user_file = open('test_users_for_prediction/' + str(user_id) + '_movies.txt', "r")
	print(user_id)

	# User rated movies ids are in ascending order
	movie_id_list_index = 0
	row_content_index = 0
	accounted = 0
	missing = 0
	row_content_aux = []

	for x in range(0,len(movies_ids_list)):
		row_content_aux.append('0')

	for entry in user_file:
		# Getting data
		movie_id = entry.split(',')[0]
		rating = entry.split(',')[1].replace('\n', '')

		# print("list 1k500 id current: " + str(movies_ids_list[movie_id_list_index]))
		# print("id user rated current: " + str(movie_id))
		# pause = input('before')

		# Filling missing rates
		if ((int(movie_id) != movies_ids_list[movie_id_list_index]) and (int(movie_id) > movies_ids_list[movie_id_list_index])):
			# Must walk in wanted id until current movie id == the wante one
			while ((int(movie_id) != movies_ids_list[movie_id_list_index]) and (int(movie_id) > movies_ids_list[movie_id_list_index])):
				if movie_id_list_index < len(movies_ids_list)-1:
					movie_id_list_index = movie_id_list_index + 1
					if row_content_index < len(movies_ids_list)-1:
							row_content_index = row_content_index + 1
					missing = missing + 1
					if int(movie_id) == movies_ids_list[movie_id_list_index]:
						# print("id found: " + str(movie_id))
						# pause = input('found')
						# Inserting actual raring
						row_content_aux[row_content_index] = rating
						if movie_id_list_index < len(movies_ids_list)-1:
							movie_id_list_index = movie_id_list_index + 1
						if row_content_index < len(movies_ids_list)-1:
							row_content_index = row_content_index + 1

						accounted = accounted + 1
		elif ((int(movie_id) != movies_ids_list[movie_id_list_index]) and (int(movie_id) < movies_ids_list[movie_id_list_index])):
			# Do nathing -> will loop through current user rating until it finds what it wanst
			pass
		elif int(movie_id) == movies_ids_list[movie_id_list_index]:
			# print("id found: " + str(movie_id))
			# pause = input('found')
			# Inserting actual raring
			row_content_aux[row_content_index] = rating
			if movie_id_list_index < len(movies_ids_list)-1:
				movie_id_list_index = movie_id_list_index + 1
			if row_content_index < len(movies_ids_list)-1:
				row_content_index = row_content_index + 1

			accounted = accounted + 1
	user_file.close()

	# print("accounted: " + str((accounted)))
	# print("missing: " + str((missing)))
	print("sum: " + str(missing + accounted))
	print("content length: " + str(len(row_content_aux)))
	# pause = input('pause')
	
	# print(row_content_aux)
	# pause = input('pause')

	content = ""
	for rating in row_content_aux:
		content += rating.replace(' ', '') + ", "

	matrix_file.write(content[:-2] + "\n")

	# print(content[:-2])
	# pause = input('pause')

print("Average missing rate per (outta the 1k500 movies most rated) user (outta the 1k most active): " + str(missing/len(user_ids_sorted)))

matrix_file.close()