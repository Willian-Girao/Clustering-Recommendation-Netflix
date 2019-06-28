#!/usr/bin/env python

import os

# Getting all files within target directory.
movies_files = os.listdir('top_1k_active_users_movies/')

# Target user id
target = '1007577'

# opening user file			
target_user_ratings = open('top_1k_active_users_movies/' + target + '_movies.txt', "r")

final_file = open('U_target_' + target + '_rated_movies.txt', "a+")

final_content = ""
line_count = 0
for line in target_user_ratings:
	line_count = line_count + 1
	content = line.split(',')
	rate = content[1].replace('\n', '')
	final_content += rate + ', '

print('Number of movies rated: ' + str(line_count))

final_file.write(final_content[:-1])
# closing final file
target_user_ratings.close()
final_file.close()