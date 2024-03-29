from django.contrib import admin
#from leaflet.admin import LeafletGeoAdmin
from .models import Place, Food, Comment, Restaurant_Type, Food_Type, City
#from .models import WeatherStation
#admin.site.register(WeatherStation, LeafletGeoAdmin)
# Register your models here.

admin.site.register(Place)
admin.site.register(Food)
admin.site.register(Comment)
admin.site.register(Restaurant_Type)
admin.site.register(Food_Type)
admin.site.register(City)


