import django_filters

from first_app.models import Coordinates

class CoordinateFilter(django_filters.FilterSet):
	lat = django_filters.NumberFilter()
	longi = django_filters.NumberFilter()
	class Meta:
		model = Coordinates