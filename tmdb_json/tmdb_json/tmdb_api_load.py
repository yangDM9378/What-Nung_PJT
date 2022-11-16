import requests
import json
TMDB_API_KEY = '1e4b49dae8c23a3ddd0dd730f5a5fa1c'
def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 100):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                fields = {
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres': movie['genre_ids'],
                    'backdrop_path': movie['backdrop_path']
                }

                data = {
                    "model": "tmdb_json.movie",
                    "pk": movie['id'],
                    "fields": fields
                }

                total_data.append(data)

    with open("movies.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)
get_movie_datas()

def get_genre_datas():
    total_data = []
    
    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=en-US"
    genres = requests.get(request_url).json()
    print(genres)
    for genre in genres['genres']:
        fields = {
            'genre_id': genre['id'],
            'name': genre['name']
        }

        data = {
            "model": "tmdb_json.genre",
            "pk": genre['id'],
            "fields": fields
        }

        total_data.append(data)

    with open("genres.json", "w", encoding="utf-8") as w:
        json.dump(total_data, w, indent="\t", ensure_ascii=False)

get_genre_datas()