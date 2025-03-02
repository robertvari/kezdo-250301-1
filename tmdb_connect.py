import tmdbsimple as tmdb
import pprint
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

poster_root = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"
backdrop_root = "https://image.tmdb.org/t/p/w1920_and_h800_multi_faces"

movies = tmdb.Movies()
popular_movies = movies.popular(page=1)
for movie in popular_movies["results"]:
    print("-"*100)
    print(movie["title"])
    print(movie["overview"])
    print(movie["release_date"])
    print(movie["vote_average"])
    print(f"{poster_root}{movie['poster_path']}")