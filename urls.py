from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
#from .views import position, find_vehicles
from .views import *


urlpatterns = {
    path('', find_vehicles, name="find_vehicles"),
    path('items/', items, name="items"),
    path('<int:vehicle_id>/position', position, name="store_position"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
