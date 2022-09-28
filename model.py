import tensorflow as tf
from tensorflow import keras
import csv
import random
import numpy as np

file = open('normalizedData.csv')
csvreader = csv.reader(file)

header = next(csvreader)

x = []
y = []

x_test = []
y_test = []

i = 0
for row in csvreader:
    i += 1
    if i%2 == 1:
        continue
    garray = []
    for j in row[2]:
        if j.isdigit():
            garray.append(int(j))
    d = []
    for g in garray:
        d.append(g)
    d.append(int(row[3]))
    d.append(int(row[4]))
    d.append(int(row[5]))
    x.append(d)
    y.append(int(row[7]))

x = np.asarray(x).astype('float32')
y = np.asarray(y).astype('float32')
x_test = np.asarray(x_test).astype('float32')
y_test = np.asarray(y_test).astype('float32')

print(len(x))
print(len(x_test))

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(22, input_dim=22, activation='relu'))
model.add(tf.keras.layers.Dense(32, activation='relu'))
model.add(tf.keras.layers.Dense(4, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x, y, epochs = 195, shuffle=True, batch_size=40, verbose=2)
# scores = model.evaluate(x_test, y_test)
# print(scores)

file = open('normalizedSeasonalData.csv')
csvreader = csv.reader(file)

header = next(csvreader)

x_pred = []
name = []
season = []

i = 0
for row in csvreader:
    i += 1
    if i%2 == 1:
        continue
    garray = []
    for j in row[2]:
        if j.isdigit():
            garray.append(int(j))
    name.append(row[1])
    d = []
    for g in garray:
        d.append(g)
    d.append(int(row[3]))
    d.append(int(row[4]))
    d.append(int(row[5]))
    x_pred.append(d)
    season.append(row[6])

x_pred = np.asarray(x_pred).astype('float32')
x_pred.reshape(1, -1)

predictions = model.predict(x_pred)

rank = {}
rank[0] = "S"
rank[1] = "A"
rank[2] = "B"
rank[3] = "F"

i = 0
curr_seas = season[0]
print(curr_seas)
while i < len(predictions):
    max_value = max(predictions[i])
    max_index = list(predictions[i]).index(max_value)
    
    if curr_seas != season[i]:
        curr_seas = season[i]
        print(curr_seas)
    print(name[i] + " IS RANK " + rank[max_index])
    i += 1