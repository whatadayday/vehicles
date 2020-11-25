import json
from django.conf import settings
import redis
from geopy.distance import great_circle
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


# connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0, decode_responses=True)

@api_view(['POST'])
def position(request, vehicle_id):
    if request.method == 'POST':
        lng = request.POST['lng']
        lat = request.POST['lat']
        coord = {
            'lng': lng,
            'lat': lat,
        }

        redis_instance.geoadd("geo", lng, lat, vehicle_id)
        response = {
            'msg': f"{vehicle_id} successfully set to {coord}"
        }
        return Response(response, 201)

@api_view(['GET'])
def find_vehicles(request):
    if request.method == 'GET':
        nearby_radius = request.GET['nearby_radius']
        lng = request.GET['lng']
        lat = request.GET['lat']

        response = {}
        for key in redis_instance.georadius("geo", lng, lat, nearby_radius):
            response[key] = redis_instance.geohash(key).copy()

        return Response(response, 201)