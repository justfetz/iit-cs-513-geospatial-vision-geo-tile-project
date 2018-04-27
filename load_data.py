import csv, sys, os

project_dir = "/Users/jasonfetzer/Desktop/djangoStuff/stockRoller"


sys.path.append(project_dir)


#settings.configure()

os.environ['DJANGO_SETTINGS_MODULE'] = 'stockRoller.settings'

import django

django.setup()

from first_app.models import Coordinates


data = csv.reader(open("/Users/jasonfetzer/Desktop/djangoStuff/stockRoller/pointcloud2.csv"), delimiter=",")


for row in data:
	if row[0] != 'latitude':
		post= Coordinates()
		post.latitude = row[0]
		post.longitude = row[1]
		post.altitude = row[2]
		post.intensity = row[3]
		post.save()






