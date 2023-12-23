from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers

class CabinViewSet(ModelViewSet):

    queryset = models.Cabin.objects.all()
    serializer_class = serializers.CabinSerializer

class GuestViewSet(ModelViewSet):

    queryset = models.Guest.objects.all()
    serializer_class = serializers.GuestSerializer

class SettingViewSet(ModelViewSet):

    queryset = models.Setting.objects.all()
    serializer_class = serializers.SettingSerializer

class BookingViewSet(ModelViewSet):

    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    
class TodoViewSet(ModelViewSet):

    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

