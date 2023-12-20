from django.db import models

class Cabin(models.Model):
    
    creted_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    # description = models.TextField()
    # image = models.CharField(max_length=255)
    # max_capacity = models.SmallIntegerField()
    # regular_price = models.DecimalField(max_digits=6, decimal_places=2)
    # discount = models.DecimalField(max_digits=6, decimal_places=3)

class Guest(models.Model):

    creted_at = models.DateTimeField(auto_now=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    nationality = models.CharField(max_length=255)
    country_flag = models.CharField(max_length=255)
    national_id_number = models.CharField(max_length=255)

class Setting(models.Model):

    creted_at = models.DateTimeField(auto_now=True)    
    min_booking_length = models.IntegerField()
    max_booking_length = models.IntegerField()
    max_guest_per_booking = models.IntegerField()
    breakfast_price = models.DecimalField(max_digits=6, decimal_places=2)

class Booking(models.Model):

    creted_at = models.DateTimeField(auto_now=True) 
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    nights_number = models.SmallIntegerField() 
    guests_number = models.SmallIntegerField()
    cabin_price = models.DecimalField(max_digits=6, decimal_places=2)
    extra_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    status = models.CharField(max_length=255)
    has_breakfast = models.BooleanField()
    is_paid = models.BooleanField()
    observations = models.TextField(null=True)
    cabin = models.ForeignKey(Cabin, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)



