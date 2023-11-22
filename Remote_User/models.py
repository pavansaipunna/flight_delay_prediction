from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class flight_delay_prediction_model(models.Model):


    Departure_Country= models.CharField(max_length=300)
    Departure_Airport= models.CharField(max_length=300)
    Flight_Name = models.CharField(max_length=300)
    names= models.CharField(max_length=300)
    Date= models.CharField(max_length=300)
    Departure_Scheduled_Time= models.CharField(max_length=300)
    Pre_Flight= models.CharField(max_length=300)
    Expected_Delay = models.IntegerField()
    Historical_Flight_Delay= models.IntegerField()
    Arrival_Country= models.CharField(max_length=300)
    Arrival_Airport= models.CharField(max_length=300)
    Airport_Delay_Reason= models.CharField(max_length=300)
    Air_Route_Delay_Reason= models.CharField(max_length=300)
    Other_Reason= models.CharField(max_length=300)

class flight_delay_model(models.Model):

    Departure_Country= models.CharField(max_length=300)
    Departure_Airport= models.CharField(max_length=300)
    Flight_Name = models.CharField(max_length=300)
    names= models.CharField(max_length=300)
    Date= models.CharField(max_length=300)
    Departure_Scheduled_Time= models.CharField(max_length=300)
    Pre_Flight= models.CharField(max_length=300)
    Expected_Delay = models.IntegerField()
    Historical_Flight_Delay= models.IntegerField()
    Total_Flight_Delay = models.IntegerField()
    Arrival_Country= models.CharField(max_length=300)
    Arrival_Airport= models.CharField(max_length=300)
    Airport_Delay_Reason= models.CharField(max_length=300)
    Air_Route_Delay_Reason= models.CharField(max_length=300)
    Other_Reason= models.CharField(max_length=300)

class review_Model(models.Model):
    uname = models.CharField(max_length=100)
    ureview = models.CharField(max_length=100)
    sanalysis = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    tname= models.CharField(max_length=300)
    feedback = models.CharField(max_length=300)

class recommend_Model(models.Model):
    uname1 = models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    dt= models.CharField(max_length=300)
    usefull= models.CharField(max_length=300)

class search_ratio_model(models.Model):
    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



