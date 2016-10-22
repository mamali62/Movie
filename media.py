import webbrowser
#define class Movie with two constructor
class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title=movie_title
		self.storyline=movie_storyline
		self.poster_image_url=poster_image
		self.trailer_youtube_url=trailer_youtube

	def show_trailer(self):#this is show and open url 
		webbrowser.open(self.trailer_youtube_url)	
