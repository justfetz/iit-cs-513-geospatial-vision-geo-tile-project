from django.contrib import admin
from import_export import resources
#from resources import CoordinateResource
from import_export.admin import ImportExportModelAdmin, ImportMixin
from first_app.models import AccessRecord, Topic, WebPage, User , Coordinates, PointOfInterest




class CoordinateResource(resources.ModelResource):
    class Meta:
        model = Coordinates
        exclude = ('id',)
        fields = ('latitude', 'longitude', 'altitude', 'intensity')
        import_id_fields=['latitude', 'longitude']


@admin.register(Coordinates)
class CoordinateAdmin(ImportExportModelAdmin):
    resource_class = CoordinateResource
    list_display = ('latitude', 'longitude', 'altitude', 'intensity')
    #pass
# Register your models here.



admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(User)
admin.site.register(PointOfInterest)
#admin.site.register(CoordinateAdmin)