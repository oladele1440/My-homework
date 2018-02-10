import os
import csv

with open('cereal.csv', 'r') as csv_file:

    file_1 = csv.reader(csv_file, delimiter=',')

    for apple in file_1: 
        print(apple)
    for orange in file_1:
        print(orange)
