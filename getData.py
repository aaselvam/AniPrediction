import requests
import json
import csv
import time

mal_ids = []
studios = []
directors = []
genres = []
og_creators = []
sources = []
animation_directors = []
composers = []
titles = []
age_rating = []
mal_score = []

for i in range(51,56):
    response = requests.get('https://api.jikan.moe/v3/top/anime/' + str(i) + '/tv?subtype=tv')
    time.sleep(2)
    if(response.status_code == 200):
        print("Page " + str(i))
        res = response.json()
        top = res["top"]

        for j in top:
            mal_ids.append(j['mal_id'])
            titles.append(j['title'].encode("utf-8"))
    else:
        print(response.status_code)

time.sleep(2)
wait_counter = 1

print("General stats starting")
for id in mal_ids:
    if(wait_counter % 30 == 0):
        print("General Stats: " + str(100*(wait_counter/len(mal_ids))) + "%")

    response = requests.get('https://api.jikan.moe/v3/anime/' + str(id) + '/')
    if(response.status_code == 200):
        res = response.json()

        #studios
        l_s = []
        for s in res['studios']:
            l_s.append(s['name'].encode("utf-8"))
        studios.append(l_s)

        #genres
        l_g = []
        for g in res['genres']:
            l_g.append(g['name'].encode("utf-8"))
        genres.append(l_g)

        #sources
        sources.append(res['source'].encode("utf-8"))

        #age_rating
        age_rating.append(res['rating'].encode("utf-8"))

        #mal_score
        mal_score.append(res['score'])
        wait_counter += 1
    else:
        studios.append("None")
        genres.append("None")
        sources.append("None")
        age_rating.append("None")
        mal_score.append("None")
        print(response.status_code)

print("General Stats done")
wait_counter = 1

time.sleep(5)

print("General Staff starting")
for id in mal_ids:
    if(wait_counter % 30 == 0):
        print("Staff Stats: " + str(100*(wait_counter/len(mal_ids))) + "%")
    
    response = requests.get('https://api.jikan.moe/v3/anime/' + str(id) + '/characters_staff')

    director_f = False
    creator_f = False
    anim_f = False
    comp_f = False

    if(response.status_code == 200):
        res = response.json()

        for staff in res['staff']:

            if "Director" in staff['positions']:
                directors.append(staff['name'].encode("utf-8"))
                director_f = True
            elif "Original Creator" in staff['positions']:
                og_creators.append(staff['name'].encode("utf-8"))
                creator_f = True
            elif "Chief Animation Director" in staff['positions']:
                animation_directors.append(staff['name'].encode("utf-8"))
                anim_f = True
            elif "Music" in staff['positions']:
                composers.append(staff['name'].encode("utf-8"))
                comp_f = True
        
        wait_counter += 1
    else:
        time.sleep(1)
        directors.append("None")
        og_creators.append("None")
        animation_directors.append("None")
        composers.append("None")
        print(response.status_code)
    
    if not director_f:
        directors.append("None")
    
    if not creator_f:
        og_creators.append("None")
    
    if not anim_f:
        animation_directors.append("None")
    
    if not comp_f:
        composers.append("None")

print("General Staff done")

#fields = ["MAL_ID", "MAL_SCORE", "MAL_TITLE", "GENRES", "STUDIOS", "DIRECTORS", "OG_CREATOR", "SOURCE", "ANIM_DIRECTOR", "COMPOSER", "AGE_RATING"]
rows = []

for i in range(len(mal_ids)):
    row = [mal_ids[i], mal_score[i], titles[i], genres[i], studios[i], directors[i], og_creators[i], 
    sources[i], animation_directors[i], composers[i], age_rating[i]]
    rows.append(row)

with open('aniData.csv', 'a') as csvfile:  
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(rows)