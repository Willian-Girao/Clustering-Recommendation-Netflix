import random, os

matrix = open('userId_X_movieId_ratings_matrix.txt', 'r')

m = []
for line in matrix:
	row_i = line.split(',')
	aux = []
	for i in row_i:
		par = i.replace('\n', '')
		par = par.replace(' ', '')
		aux.append(int(par))
	m.append(aux)

rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

out_matrix = open('movieId_X_userId_ratings_matrix.txt', 'a+')

rows_count = 0
for row in rez:
	content = ""
	rows_count = rows_count + 1
	for user_rating in row:
		content += str(user_rating) + ", "
	out_matrix.write(content[:-2] + "\n")
out_matrix.close()

print("Rows: " + str(rows_count))
print("Columns: " + str(len(rez[0])))
	