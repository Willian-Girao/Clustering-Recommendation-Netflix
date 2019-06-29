#### Dataset generated from the original Netflix dataset

This dataset is a subset of the original dataset. This dataset consists of two subsets of the original dataset's users and movies, where the **users** are the top **1,000 most active users** (a.k.a. have rated various movies), and the **movies** are the **top 1,000 most rated** ones. The total amount of ratings within this dataset is **x,xxx,xxx**.

#### top_1k_active_users.txt

Text file containing the list of user ids and their respective ratings count. The structure of each file is 'movied_id, rate'. Users amount of ratings varies from **2,087** up to **1,7653**.

If the file looks like:

```
305344, 17653
387418, 17436
2439493, 16565
...
```
we know that the user  with id 305344 have rated 17653 movies, and so on.

#### top_1k_rated_movies.txt

Text file containing the list of movies ids and their respective total amount of ratings. The structure 
of each file is 'movied_id, number_of_ratings, average_rating'. Movies ratings count varies from **2,5873** up to **23,2944**.

If the file looks like:

```
5317, 232944, 3.36
15124, 216596, 3.72
14313, 200832, 3.78
...
```

we know that the movie with id 5317 have had 232944 ratings and have average rating of 3.36, and so on.