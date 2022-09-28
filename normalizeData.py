import csv
import gmpy2
import numpy as np


# anime_id = []
# anime_name = []
# anime_genres = []
# anime_sources = []
# anime_studios = []
# anime_score = []
# anime_rank = []

genres = {}
studios = {}
sources = {}

genres["'Action'"] = 0
genres["'Adventure'"] = 1
genres["'Drama'"] = 2
genres["'Fantasy'"] = 3
genres["'Comedy'"] = 4
genres["'Sci-Fi'"] = 5
genres["'Suspense'"] = 6
genres["'Romance'"] = 7
genres["'Supernatural'"] = 8
genres["'Slice of Life'"] = 9
genres["'Mystery'"] = 10
genres["'Sports'"] = 11
genres["'Award Winning'"] = 12
genres["'Ecchi'"] = 13
genres["'Avant Garde'"] = 14
genres["'Horror'"] = 15
genres["'Boys Love'"] = 16
genres["'Gourmet'"] = 17
genres["'Girls Love'"] = 18

studio_counter = 1
source_counter = 0

rank_counter = 0

file = open('data.csv')
csvreader = csv.reader(file)

header = next(csvreader)

f = open('normalizedData.csv', 'w')

writer = csv.writer(f)

r = ['anime_id', 'anime_name', 'genre_array', 'source_score', 'studio_score', 'mal_score', 'ranked_score']
writer.writerow(r)

i = 0
c = 0
for row in csvreader:
    if i == 1300: #S
        rank_counter += 1
    elif i == 6300: #A
        rank_counter += 1
    elif i == 10300: #B
        rank_counter += 1

    i += 1
    if i%2 == 1:
        continue    

    garray = [0]*19
    g_str = row[2][1:-1]
    g_str.replace('[', '')
    g_str.replace(']', '')
    for g in list(g_str.split(", ")):
        garray[genres[g]] = 1
    
    if row[3] not in sources:
        source_counter += 1
        sources[row[3]] = source_counter


    k = 0
    sarray = [0, 0]
    s_str = row[4][1:-1]
    if len(list(s_str.split(", "))) < 3:
        for st in list(s_str.split(", ")):
            if st not in studios:
                studios[st] = studio_counter
                studio_counter += 1
            sarray[k] = studios[st]
            k += 1

    nRow = [row[0], row[1], garray, sources[row[3]], sarray[0], sarray[1], row[5], rank_counter]
    writer.writerow(nRow)

np.save("studioDict.npy", studios)
np.save("sourceDict.npy", sources)
np.save("genresDict.npy", genres)