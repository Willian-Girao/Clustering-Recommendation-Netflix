import numpy as np
import matplotlib.pyplot as plt

target = 'top_1k_active_users.txt'

file = open(target, "r")

ids = []
ratings = []

for line in file:
	user_id = line.split(',')[0]
	ratingsCount = (line.split(',')[1].replace('\n', '')).replace(' ', '')

	ids.append(int(user_id))
	ratings.append(int(ratingsCount))

file.close()

x = ids
y = ratings


plt.title('Amount of rated movies among the top 1k avtive users')
plt.xlabel('User id')
plt.ylabel('Ratings count')

plt.plot(x,y)
# plt.xticks(np.arange(min(x), max(x)+1, 1.0))
plt.show()

# plt.scatter(x, y)
# plt.show()
