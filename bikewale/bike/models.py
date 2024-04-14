from django.db import models

# Create your models here.

class Bike(models.Model):
    bike_id=models.AutoField()
    bike_name = models.CharField()
    description = models.TextField()
    short_url=models.CharField()
    seo_name=models.SlugField()
    is_popular=models.BooleanField()
    is_trending = models.BooleanField()
    short_description=models.TextField()
    created_by = models.CharField()
    modified_by = models.CharField()
    created_on = models.DateTimeField()
    modified_on = models.DateTimeField()
    
    
    
class Brand(models.Model):
    id=models.IntegerField()
    name=models.CharField()
    full_name=models.CharField()
    description=models.TextField()
    url=models.CharField()
    image_url=models.CharField()
    short_url=models.CharField()
    seo_name=models.SlugField()
   
  