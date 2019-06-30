#!/usr/bin/env python

# Script maps from final training user's id to original dataset user's id

final_file = open("mapped_user_ids.txt", "a+")

user_list = open("top_1k_active_users_sorted.txt", "r")

id_counter = 1

for line in user_list:
	user_id = line.split(',')[0]
	final_file.write(user_id + ", " + str(id_counter) + "\n") 	
	print(user_id + " => " + str(id_counter))
	id_counter = id_counter + 1

final_file.close()
user_list.close()

