import tmdbsimple as tmdb
import os, requests
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

poster_root = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"
backdrop_root = "https://image.tmdb.org/t/p/w1920_and_h800_multi_faces"
# r = raw string
posters_local_cache = "D:/Work/PythonSuli/kezdo-250301/tmdb_posters"


movies = tmdb.Movies()
popular_movies = movies.popular(page=1)

for movie in popular_movies["results"]:
    print("-"*100)
    print(movie["title"])
    print(movie["overview"])
    print(movie["release_date"])
    print(movie["vote_average"])

    # download poster if not exists
    poster_file_path = f"{posters_local_cache}{movie['poster_path']}"
    if not os.path.exists(poster_file_path):
        poster_url = f"{poster_root}{movie['poster_path']}"
        poster_data = requests.get(poster_url).content
        print(f"Downloading poster: {poster_file_path}")

        with open(poster_file_path, "wb") as file:
            file.write(poster_data)