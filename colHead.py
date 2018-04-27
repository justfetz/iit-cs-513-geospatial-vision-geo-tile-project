

#!python3
import csv
with open('pointcloud2.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('pointcloud2.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['latitude','longitude', 'altitude', 'intensity'])
    w.writerows(data)