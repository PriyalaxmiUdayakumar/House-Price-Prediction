from django.db import models

# Create your models here.
class Packages(models.Model):
    location=models.CharField(max_length=60)
    img=models.ImageField(upload_to="pictures")
    price=models.IntegerField()
    
class Prediction(models.Model):
    bedroom=models.IntegerField()
    bathroom=models.IntegerField()
    sqft_living=models.IntegerField()
    sqft_above=models.IntegerField()
    yr_built=models.IntegerField()
    yr_renovated=models.IntegerField()
    view=models.IntegerField()
    floors=models.IntegerField()
    lat=models.IntegerField()
    long=models.IntegerField()
    waterfront=models.IntegerField()
    grade=models.IntegerField()