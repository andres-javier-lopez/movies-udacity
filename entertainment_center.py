"""Creates and shows the movie website.

This is the main module for the creation of the movie website. The list of
movies are loaded from the movies module and the process to create the site is
loaded from the fresh_tomatoes module.

This module only executes itself when is called as the main module, and won't
do anything when imported.
"""

import fresh_tomatoes
import movies


if __name__ == '__main__':
    fresh_tomatoes.open_movies_page(movies.movies)
