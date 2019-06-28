/* Test dataset generate from the Netflix dataset */

	This dataset is a subset of the original dataset. It contains the top 1k most
active users (bigger count of ratings) and their respective ratings list.

## ./top_1k_active_users

The folder './top_1k_active_users' contains 1000 text files named 'xxx_movies.txt', 
where 'xxx' is the id of a user. The sctructure of each file is 'movied_id, rate'.

For instance, if the file '1001143_movies.txt' contains:

289, 5
429, 5
483, 4
550, 5

we know that the user  with id 1001143 has given rate 5 for the movie with id 289, and so on.

## 1k_top_active_users.txt

Text file contaning the list of user ids and their respective ratings count. The sctructure 
of each file is 'movied_id, rate'.


305344, 17653
387418, 17436
2439493, 16565
1664010, 15813
2118461, 14831

we know that the user  with id 305344 have rated 17653 movies, and so on.




