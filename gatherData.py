import requests
import csv
import time

anime_id = []
anime_name = []
anime_genres = []
anime_source = []
anime_studios = []
anime_score = []

i = 1

while i < 401:
    params = {
        'page': i
    }
    r = requests.get("https://api.jikan.moe/v4/top/anime", params=params)

    if r.status_code != 200:
        print("woah")
        time.sleep(3)
        continue
    
    i += 1

    data = r.json()['data']

    for anime in data:
        anime_id.append(anime['mal_id'])

        anime_name.append(anime['title'])

        anime_source.append(anime['source'])

        anime_score.append(anime['score'])

        g = []
        for genre in anime['genres']:
            g.append(genre['name'])
        anime_genres.append(g)

        s = []
        for studio in anime['studios']:
            s.append(studio['name'])
        anime_studios.append(s)
    
f = open('data.csv', 'w')

writer = csv.writer(f)
r = ['anime_id', 'anime_name', 'anime_genres', 'anime_source', 'anime_studios', 'anime_score']
writer.writerow(r)

for i in range(len(anime_id)):
    if (len(anime_genres[i]) == 0 or len(anime_studios[i]) == 0):
        print("lost anime: " + anime_name[i])
        continue

    row = [anime_id[i], anime_name[i], anime_genres[i], anime_source[i], anime_studios[i], anime_score[i]]
    
    try:
        writer.writerow(row)
    except:
        print("lost anime: " + anime_name[i])

