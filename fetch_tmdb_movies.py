import os
import requests
import csv
import time
from dotenv import load_dotenv

load_dotenv()
TMDB_API_KEY = os.getenv('TMDB_API') or os.getenv('TMDB_API_KEY')
TMDB_BASE = 'https://api.themoviedb.org/3'
POSTER_BASE = 'https://image.tmdb.org/t/p/w500'

# Get all genres
resp = requests.get(f'{TMDB_BASE}/genre/movie/list', params={'api_key': TMDB_API_KEY, 'language': 'en-US'})
genres = resp.json()['genres']
genre_map = {g['id']: g['name'] for g in genres}

movies = []
seen_ids = set()

for genre in genres:
    genre_id = genre['id']
    genre_name = genre['name']
    for page in range(1, 4):  # 3 pages x ~20 = ~60 movies per genre
        try:
            r = requests.get(f'{TMDB_BASE}/discover/movie', params={
                'api_key': TMDB_API_KEY,
                'with_genres': genre_id,
                'sort_by': 'popularity.desc',
                'page': page,
                'language': 'en-US',
            })
            time.sleep(0.25)
        except Exception as e:
            print(f"Error fetching discover for genre {genre_name} page {page}: {e}")
            continue
        for m in r.json().get('results', []):
            if m['id'] in seen_ids or not m.get('poster_path'):
                continue
            seen_ids.add(m['id'])
            # Get details for director, cast, runtime, language
            try:
                details = requests.get(f'{TMDB_BASE}/movie/{m["id"]}', params={'api_key': TMDB_API_KEY, 'language': 'en-US'}).json()
                time.sleep(0.25)
                credits = requests.get(f'{TMDB_BASE}/movie/{m["id"]}/credits', params={'api_key': TMDB_API_KEY}).json()
                time.sleep(0.25)
            except Exception as e:
                print(f"Error fetching details/credits for movie {m['title']} ({m['id']}): {e}")
                continue
            director = ''
            for crew in credits.get('crew', []):
                if crew['job'] == 'Director':
                    director = crew['name']
                    break
            cast = ', '.join([c['name'] for c in credits.get('cast', [])[:5]])
            movies.append({
                'title': m['title'],
                'summary': m.get('overview', ''),
                'year': m.get('release_date', '')[:4],
                'genre': genre_name,
                'director': director,
                'cast': cast,
                'duration': details.get('runtime', ''),
                'language': details.get('original_language', ''),
                'poster_url': POSTER_BASE + m['poster_path'],
                'country': ', '.join([c['iso_3166_1'] for c in details.get('production_countries', [])]),
            })

# Save to CSV
with open('data/movies.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title','summary','year','genre','director','cast','duration','language','poster_url','country'])
    writer.writeheader()
    for m in movies:
        writer.writerow(m)

print(f"Saved {len(movies)} movies to data/movies.csv") 