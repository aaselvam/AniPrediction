import tensorflow as tf
import csv
import random

file = open('normalizedData.csv')
csvreader = csv.reader(file)

header = next(csvreader)

x = []
y = []

i = 0
for row in csvreader:
    i += 1
    if i%2 == 1:
        continue
    else:
        garray = []
        for j in row[2]:
            if j.isdigit():
                garray.append(int(j))
        x.append([garray, int(row[3]), int(row[4])])
        y.append(int(row[6]))

