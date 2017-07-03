import webbrowser

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
    
class Movie(Video):
    """This class accepts and provides Movie show information"""

    def __init__(self, title, storyline, posterImage, trailerYoutube):
        Video.__init__(self, title, storyline, posterImage, trailerYoutube)

class TvShow(Video):
    """This class accepts and provides TV show information"""

    def __init__(self, title, storyline, posterImage, trailerYoutube):
        Video.__init__(self, title, storyline, posterImage, trailerYoutube)