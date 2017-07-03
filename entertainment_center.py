#Initial imports to use classes and functions
import media
import fresh_tomatoes

#Movie database for the website in format title, story description, poster image, and trailer video
prisoners=media.Movie("Prisoners",
"A daughter goes missing and two people use their own means to find her",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTg0NTIzMjQ1NV5BMl5BanBnXkFtZTcwNDc3MzM5OQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
"https://www.youtube.com/watch?v=KWhS0xN3C0g")

noCountryForOldMen=media.Movie("No Country For Old Men",
"A man finds a stash of money, but is shortly pursued by an unstoppable force",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5Njk3MjM4OV5BMl5BanBnXkFtZTcwMTc5MTE1MQ@@._V1_.jpg",
"https://www.youtube.com/watch?v=38A__WT3-o0")

sicario=media.Movie("Sicario",
"A FBI agent is recruited into a shady team of operatives who's methods are not textbook",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5NjM3NTk1M15BMl5BanBnXkFtZTgwMzg1MzU2NjE@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
"https://www.youtube.com/watch?v=sR0SDT2GeFg")

#Insert the instances into a list for 'open_movie_page' to read
movies=[prisoners, noCountryForOldMen, sicario]
#Render HTML code for the website
fresh_tomatoes.open_movies_page(movies)