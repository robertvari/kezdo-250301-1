import tmdbsimple as tmdb
import os, requests, json
tmdb.API_KEY = '83cbec0139273280b9a3f8ebc9e35ca9'
tmdb.REQUESTS_TIMEOUT = 5

poster_root = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"
backdrop_root = "https://image.tmdb.org/t/p/w1920_and_h800_multi_faces"
posters_local_cache = "D:/Work/PythonSuli/kezdo-250301/tmdb_posters"
movie_dada_cache = "D:/Work/PythonSuli/kezdo-250301/tmdb_posters/movie_data.json"

movies = tmdb.Movies()
popular_movies = movies.popular(page=1)

movie_data = {}
for movie in popular_movies["results"]:
    movie_data[movie["id"]] = {
        "title": movie["title"],
        "overview": movie["overview"],
        "release_date": movie["release_date"],
        "vote_average": movie["vote_average"]
    }

    # download poster if not exists
    poster_file_path = f"{posters_local_cache}{movie['poster_path']}"
    if not os.path.exists(poster_file_path):
        poster_url = f"{poster_root}{movie['poster_path']}"
        poster_data = requests.get(poster_url).content
        print(f"Downloading poster: {poster_file_path}")

        with open(poster_file_path, "wb") as file:
            file.write(poster_data)

print("Saving movie_data...")
with open(movie_dada_cache, "w") as file:
    json.dump(movie_data, file)