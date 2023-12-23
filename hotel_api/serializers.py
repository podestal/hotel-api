from rest_framework import serializers
from . import models

class CabinSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cabin
        fields = '__all__'

class GuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Guest
        fields = '__all__'

class SettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Setting
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Booking
        fields = '__all__'

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Todo
        fields = '__all__'