#Initial import for one of the lessons for the function 'showTrailer'
import webbrowser

#Class video allows instances to be made of a movie for __doc__.
#I made this into a parent class as the last lesson describes using TV shows as well
class Video():
    #__doc__ contents
    """This class accepts and provides video information"""
    
    #global variables for methods inside Video class
    VALID_RATINGS=['G','PG','PG-13','R']

    #Initializing constructor to create video instances
    def __init__(self, title, storyline, posterImage, trailerYoutube):
        self.title=title
        self.storyline=storyline
        self.poster_image_url=posterImage
        self.trailer_youtube_url=trailerYoutube

    #Method to show trailer without the website generator
    def showTrailer(self):
        webbrowser.open(self.trailerYoutubeURL)

#The children classes for the Video class. For convenience of not having to write code again.
#Hope you don't mind reading a bit more code...
class Movie(Video):
    #__doc__ contents
    """This class accepts and provides Movie show information"""

    #Initializing constructor to create movie instances
    def __init__(self, title, storyline, posterImage, trailerYoutube):
        Video.__init__(self, title, storyline, posterImage, trailerYoutube)

class TvShow(Video):
    """This class accepts and provides TV show information"""

    def __init__(self, title, storyline, posterImage, trailerYoutube):
        Video.__init__(self, title, storyline, posterImage, trailerYoutube)