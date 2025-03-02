import tmdbsimple as tmdb
import pprint
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

poster_root = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"
backdrop_root = "https://image.tmdb.org/t/p/w1920_and_h800_multi_faces"

movie = tmdb.Movies(950396)
response = movie.info()
pprint.pprint(response)
print(f"{poster_root}{response['poster_path']}")
print(f"{backdrop_root}{response['backdrop_path']}")