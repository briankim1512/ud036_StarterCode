#Initial import for one of the lessons for the function 'showTrailer'
import webbrowser

#Class video allows instances to be made of a movie for __doc__.
#I made this into a parent class as the last lesson describes using TV shows as well
class Video():
    """This class accepts and provides video information"""
    
    VALID_RATINGS=['G','PG','PG-13','R']

    def __init__(self, title, storyline, posterImage, trailerYoutube):
        self.title=title
        self.storyline=storyline
        self.poster_image_url=posterImage
        self.trailer_youtube_url=trailerYoutube

    def showTrailer(self):
        webbrowser.open(self.trailerYoutubeURL)

#The children classes for the Video class. For convenience of not having to write code again.
#Hope you don't mind reading a bit more code...
class Movie(Video):
    """This class accepts and provides Movie show information"""

    def __init__(self, title, storyline, posterImage, trailerYoutube):
        Video.__init__(self, title, storyline, posterImage, trailerYoutube)

class TvShow(Video):
    """This class accepts and provides TV show information"""

    def __init__(self, title, storyline, posterImage, trailerYoutube):
        Video.__init__(self, title, storyline, posterImage, trailerYoutube)