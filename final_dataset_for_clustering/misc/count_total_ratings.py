#!/usr/bin/env python

import os


training_files = os.listdir('top_1k_active_users/')
count = 0

for file in training_files:	
	open_file = open('top_1k_active_users/' + file, "r")
	for line in open_file:
		count = count + 1
	open_file.close()
	print(file)
print("Total number of ratings: " + str(count))

