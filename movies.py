"""List of movies that apperar on the website.

To add a new movie to the database just append at the end of the file the 
following code, replacing the names with the right ones.

movies.append(media.Movie(
    "Movie Title",
    "This is the movie description",
    "http://example.com/movie_poster.jpg",
    "https://www.youtube.com/watch?v=TRAILER_ID",
    year='19xx', director='Director Name',
    actors=['Some Actor', 'Some Actress']
))

The named parameters year, director and actors are optional and can be omitted
if you want.
"""

import media

# start with an empty list and start filling it over
movies = []

# Start movie list, add new movies at bottom
movies.append(media.Movie(
    "Toy Story",
    "A story about a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
    year='1995', director='John Lasseter',
    actors=['Buzz', 'Woody']
))

movies.append(media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://www.movieposter.com/posters/archive/main/98/MPW-49433",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
))

movies.append(media.Movie(
    "Matrix",
    "A virtual world governed by machines",
    "https://www.movieposter.com/posters/archive/main/9/A70-4902",
    "https://www.youtube.com/watch?v=vKQi3bBA1y8"
))

movies.append(media.Movie(
    "Ratatouille",
    "A rat is a chef in Paris",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk"
))

movies.append(media.Movie(
    "Avengers",
    "A lot of superheroes in one movie",
    "http://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8"
))

movies.append(media.Movie(
    "How to train your dragon",
    "A viking befriends a dragon",
    "http://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
    "www.youtube.com/watch?v=oKiYuIsPxYk"
))

# Add new movies in this space
#
#movies.append(media.Movie(
#    "Movie Title",
#    "This is the movie description",
#    "http://example.com/movie_poster.jpg",
#    "https://www.youtube.com/watch?v=TRAILER_ID",
#    year='19xx', director='Director Name',
#    actors=['Some Actor', 'Some Actress']
#))

# End of movie list
