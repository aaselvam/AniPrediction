import requests
import csv
import time


anime_id = []
anime_name = []
anime_genres = []
anime_source = []
anime_studios = []
anime_score = []

last_page = 2
years = ["2022", "2022", "2022"]
seasons = ["spring", "summer", "fall"]

seasonals = []

counter = 0

while counter < len(years):
    i = 1
    while i < last_page:
        params = {
            'page': i
        }
        r = requests.get("https://api.jikan.moe/v4/seasons/" + years[counter] + "/" + seasons[counter], params=params)

        if r.status_code != 200:
            print("woah")
            time.sleep(3)
            continue
        
        i += 1

        last_page = int(r.json()['pagination']['last_visible_page'])

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
            seasonals.append(seasons[counter])
    counter += 1
        
f = open('seasonaldata.csv', 'w')

writer = csv.writer(f)
r = ['anime_id', 'anime_name', 'anime_genres', 'anime_source', 'anime_studios', 'season']
writer.writerow(r)

for i in range(len(anime_id)):
    if (len(anime_genres[i]) == 0 or len(anime_studios[i]) == 0):
        print("lost anime: " + anime_name[i])
        continue

    row = [anime_id[i], anime_name[i], anime_genres[i], anime_source[i], anime_studios[i], seasonals[i]]
    
    try:
        writer.writerow(row)
    except:
        print("lost anime: " + anime_name[i])

