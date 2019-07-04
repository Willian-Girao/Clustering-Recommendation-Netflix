import numpy as np
import matplotlib.pyplot as plt

target = 'top_1k500_rated_movies_sorted.txt'

file = open(target, "r")

ids = []
ratings = []

for line in file:
	movie_id = line.split(',')[0]
	avgRate = (line.split(',')[2].replace('\n', '')).replace(' ', '')

	ids.append(int(movie_id))
	ratings.append(float(avgRate))

file.close()

x = ids
y = ratings


plt.title('Average ratings per movies among the top 1k500 most rated')
plt.xlabel('Movie id')
plt.ylabel('Average rate')

plt.plot(x,y)
# plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.show()

# plt.scatter(x, y)
# plt.show()
