import media
import fresh_tomatoes

prisoners=media.Movie("Prisoners",
"A daughter goes missing and two people use their own means to find her",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTg0NTIzMjQ1NV5BMl5BanBnXkFtZTcwNDc3MzM5OQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
"https://www.youtube.com/watch?v=KWhS0xN3C0g")

noCountryForOldMen=media.Movie("No Country For Old Men",
"A man finds a stash of money, but is shortly pursued by an unstoppable force",
"https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5Njk3MjM4OV5BMl5BanBnXkFtZTcwMTc5MTE1MQ@@._V1_.jpg",
"https://www.youtube.com/watch?v=38A__WT3-o0")

movies=[prisoners, noCountryForOldMen]
fresh_tomatoes.open_movies_page(movies)