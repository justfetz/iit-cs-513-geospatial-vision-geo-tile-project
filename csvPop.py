with open(/Users/jasonfetzer/Desktop/djangoStuff/stockRoller/static/csvFiles/) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Coordinates.objects.get_or_create(
                latitude=row[0],
                longitude=row[1],
                altitude=row[2],
                intensity=row[3],
                )