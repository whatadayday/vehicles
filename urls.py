from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import position, find_vehicles
#import .views


urlpatterns = {
    path('<int:vehicle_id>/position', position, name="store_position"),
    path('', find_vehicles, name="find_vehicles"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
