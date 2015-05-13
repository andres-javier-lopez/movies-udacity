# Movie Trailer Website

This is a python project designed to create a static website that contains a 
list of movies provided by a dynamic data storage.

## Dependencies

This software only needs a python installation to run.

## Configuration

The list of movies included on the website is loaded from the movies.py file. To
add a new movie, add the following code to the movies.py file, replacing it with
the right values:

`movies.append(media.Movie(
    "Movie Title",
    "This is the movie description",
    "http://example.com/movie_poster.jpg",
    "https://www.youtube.com/watch?v=TRAILER_ID",
    year='19xx', director='Director Name',
    actors=['Some Actor', 'Some Actress']
))`

## Execution

To create the website, run the entertainment_center.py module with python. You 
can execute it from the comand line as `python entertainment_center.py`.

A file named fresh_tomatoes.html will be created and your default web browser 
will automatically open it.

If you want to make changes to the movies, edit the movies.py file and run again
the entertainment_center.py file. This will rebuild the fresh_tomatoes.html 
file.

## Contact

This project was created by Andrés Javier López (ajavier.lopez@gmail.com) as 
part of the Full Stack Developer Nanodegree on Udacity.
