import csv
import numpy as np

studios = np.load('studioDict.npy',allow_pickle='TRUE').item()
genres = np.load('genresDict.npy',allow_pickle='TRUE').item()
sources = np.load('sourceDict.npy',allow_pickle='TRUE').item()

file = open('seasonalData.csv')
csvreader = csv.reader(file)

header = next(csvreader)

f = open('normalizedSeasonalData.csv', 'w')

writer = csv.writer(f)

r = ['anime_id', 'anime_name', 'genre_array', 'source_score', 'studio1', 'studio2', 'season']
writer.writerow(r)

i = 0
for row in csvreader:
    i += 1
    if i%2 == 1:
        continue    

    garray = [0]*19
    g_str = row[2][1:-1]
    g_str.replace('[', '')
    g_str.replace(']', '')
    for g in list(g_str.split(", ")):
        garray[genres[g]] = 1
    
    k = 0
    sarray = [0, 0]
    s_str = row[4][1:-1]
    if len(list(s_str.split(", "))) < 3:
        for st in list(s_str.split(", ")):
            if st not in studios:
                continue
            sarray[k] = studios[st]
            k += 1
    
    nRow = [row[0], row[1], garray, sources[row[3]], sarray[0], sarray[1], row[5]]
    writer.writerow(nRow)