### Dataset generated from the original Netflix dataset

This dataset is a subset of the original dataset. This dataset consists of two subsets of the original dataset's users and movies, where the **users** are the top **1,000 most active users** (a.k.a. have rated various movies), and the **movies** are the **top 1,500 most rated** ones. The total amount of ratings within this dataset is **1,033,708**.

#### top_1k_active_users.arff

Text file containing the list of user ids and their respective ratings count. Users amount of ratings varies from **2,087** up to **17,653**.

```
@relation userId_ratingsCount

@attribute user_id numeric
@attribute ratings_count numeric

@data
305344, 17653
387418, 17436
...
```

#### top_1k500_rated_movies.arff

Text file containing the list of movies ids and their respective total amount of ratings as well as their average rate. Movies ratings count varies from **16,025** up to **232,944**.

```
@relation movieId_ratingsCount_averageRate

@attribute movie_id numeric
@attribute ratings_count numeric
@attribute average_rate numeric

@data
5317, 232944, 3.36
15124, 216596, 3.72
...
```