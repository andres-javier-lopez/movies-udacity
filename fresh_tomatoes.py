"""Module for construction of the movie website.

This module contains the required functions that constructs the movie website,
based on the templates provided on the templates module.
"""

import os
import re
import webbrowser

import templates


def create_movie_tiles_content(movies):
    """Creates the movie information for the websites.

    This function takes a lists of movies and transform them into a list of
    movies formatted on html, ready to be appeneded into a website.

    Args:
        movies: list of objects media.Movie that represents the list of movies

    Returns:
        Returns the list of movies formatted on html, based on the template for
        movie tiles.
    """
    # The HTML content for this section of the page
    content_list = []
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+',
                                     movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url
        )

        if youtube_id_match:
            trailer_youtube_id = youtube_id_match.group(0)
        else:
            trailer_youtube_id = None
        
        # Append the year to the title if provided
        if movie.year:
            movie_title = '%s (%s)' % (movie.title, movie.year)
        else:
            movie_title = movie.title
        
        # Add the director info if provided
        if movie.director:
            director = '<br/><small>a film by %s</small>' % movie.director
        else:
            director = ''
        
        # If actors are provided, create an actor list
        actors_list = []
        for actor in movie.actors:
            actors_list.append(actor + '<br/>')
        if actors_list:
            actors_str = ''.join(actors_list)
            actors = templates.MOVIE_TILE_ACTORS.format(
                movie=movie.title.replace(' ', '-').lower(),
                actors_list=actors_str
            )
        else:
            actors = ''
        
        # Append the tile for the movie with its content filled in
        content_list.append(templates.MOVIE_TILE_CONTENT.format(
            movie_title=movie_title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            year=movie.year,
            director=director,
            actors=actors
        ))
    content = ''.join(content_list)
    return content


def open_movies_page(movies):
    """Creates and open a movie website with the provided movies.

    This function creates an html file that lists the movies provided and then
    open the file on a web browser.

    Args:
        movies: list of objects media.Movie that represents the movies for the
          website.
    """
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual
    # dynamically generated content
    rendered_content = templates.MAIN_PAGE_CONTENT.format(
        movie_tiles=create_movie_tiles_content(movies)
    )

    # Output the file
    try:
        output_file.write(templates.MAIN_PAGE_HEAD + rendered_content)
    finally:
        output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
