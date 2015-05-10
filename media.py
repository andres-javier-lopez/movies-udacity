"""Data structures for the movie website project.

This module contains the data structures needed to store the information for 
the movie website project.
"""

import webbrowser


class Movie(object):
    """Represents a movie that will be showed on the website.
    
    This class contains all the information needed to create a movie in the 
    website.
    
    Attributes:
        title: The movie title.
        storyline: A short sentence that describes the movie storyline.
        poster_image_url: A url that links to the poster of the movie.
        trailer_youtube_url: A url to the movie trailer on YouTube.
    """
    
    def __init__(self, movie_title, movie_storyline, movie_poster,
                 movie_trailer):
        """Initializes a new movie.
        
        Initializes a movie with the attributes that will be showed on the 
        website.
        
        Args:
            movie_title: Title of the movie.
            movie_storyline: A short sentence describing the storyline of the 
              movie.
            movie_poster: An url linking to a poster of the movie.
            movie_trailer: An ulr to the movie trailer on YouTube.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        """Opens the movie trailer on a webbrowser.
        
        This function opens the operating system default webbrowser and shows 
        the movie trailer on it when called.
        """
        webbrowser.open(self.trailer_youtube_url)
