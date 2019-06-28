#!/usr/bin/env python
import os
import csv


target_file = open("1k_top_active_users.txt","r")

n_rates = 0
for line in target_file:
	amount = int(line.split(',')[1])
	print(type(amount))
	n_rates += n_rates + amount

# print('Total ratings count for top 1k users: ' + str(n_rates))
print(n_rates)

# closing final file
target_file.close()
	