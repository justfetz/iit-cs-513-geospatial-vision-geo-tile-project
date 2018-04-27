from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord, Coordinates
from . import forms
import math
from . import tilePython
from tablib import Dataset
import json
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

def index(request):
	#return render(request, 'first_app/templates/helloHTML.html')
	webPageList = AccessRecord.objects.order_by('date')
	my_dict = {'insert_me':"Hello Insertion, now I am in first_app"}
	date_dict = {'access_records':webPageList}
	#return HttpResponse("Hello There stockroller!")
	return render(request, "first_app/index.html", context = date_dict)

def indexOriginal(request):
	coordinateList = Coordinates.objects.order_by('longitude')[:1000]
	tup_dict = {'coords':coordinateList}
	return render(request, "first_app/indexOriginal.html", context=tup_dict)

def map(request):
	return render(request, 'first_app/map.html')

#def inventory(request):
#	return render(request, 'first_app/inventory.html')

#def base(request):
#	return render(request, 'first_app/base.html')

def form_name_view(request):
	form = forms.FormName()
	return render(request, 'first_app/forms.html', {'form':form})

def GeoViewForm(request):
	coordinateList = Coordinates.objects.order_by('longitude')[:1000]
	tup_dict = {'coords':coordinateList}
	#coord_json = json.dumps(list(coordinateList), cls=DjangoJSONEncoder)
	return render(request, "first_app/geo.html", context=tup_dict)
	#hello = TileSystem()


	form = forms.GeoForm()
	return render(request, 'first_app/geo.html', {'form':form})
	#class Meta:


#def base2(request):
#	return render(request, 'first_app/base2.html')

def about(request):
	return render(request, 'first_app/about.html')


def simple_upload(request):
    if request.method == 'POST':
        person_resource = CoordinateResource()
        dataset = Dataset()
        new_coordinates = request.FILES['myfile']

        imported_data = dataset.load(new_coordinates.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'first_app/simple_upload.html')



def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})

def lat_list(request):
	coords = Coordinates.object.all()
	filter = CoordinateFilter(request.GET, queryset = coords)
	return render(request, 'first_app/my_template.html', {'filter' : filter})

def coordList(request):
	coords = Coordinates.objects.all()
	context = {
	
	}

def originalProject(request):
	return render(request, 'first_app/originalProject.html')

def testSnap(request):
	return render(request, 'first_app/testSnap.html')

