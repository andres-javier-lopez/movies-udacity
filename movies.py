"""List of movies that apperar on the website.
"""

import media

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        year='1995', director='John Lasseter',
                        actors=['Buzz', 'Woody'])

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49433",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

matrix = media.Movie("Matrix",
                     "A virtual world governed by machines",
                     "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

avengers = media.Movie("Avengers",
                       "A lot of superheroes in one movie",
                       "http://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

train_dragon = media.Movie("How to train your dragon",
                           "A viking befriends a dragon",
                           "http://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
                           "www.youtube.com/watch?v=oKiYuIsPxYk")

movies = [toy_story, avatar, matrix, ratatouille, avengers, train_dragon]
