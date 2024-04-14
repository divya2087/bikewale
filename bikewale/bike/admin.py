from django.contrib import admin
from bike.models import Bike
from brand.models import Brand

class BikeAdmin(admin.ModelAdmin):
    list_display=("bike_id","bike_name","description","short_url","seo_name","is_popular","is_trending","short_description",
                  "created_by","modified_by","created_on","modified_on")
    
    admin.site.register(Bike,BikeAdmin)
    
    
class BrandAdmin(admin.ModelAdmin):
    list_display=("id","name","full_name","description","url","image_url","short_url","seo_name")

admin.site.register(Brand,BrandAdmin)


    



# Register your models here.

