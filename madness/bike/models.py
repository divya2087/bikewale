from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Bike(BaseModel):
    id=models.IntegerField()
    name = models.CharField()
    description = models.TextField()
    short_url=models.CharField()
    seo_name=models.SlugField()
    is_popular=models.BooleanField()
    is_trending = models.BooleanField()
    short_description=models.TextField()
    created_by = models.CharField(max_length=255)
    modified_by = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    
    
class Brand(BaseModel):
    id=models.IntegerField()
    name=models.CharField()
    full_name=models.CharField()
    description=models.TextField()
    url=models.CharField()
    image_url=models.CharField()
    short_url=models.CharField()
    seo_name=models.SlugField()
    
    
class BikeVariant(BaseModels):
    id=models.IntegerField()
    name = models.CharField()
    model_name=models.CharField()
    color=models.CharField()
    is_electric=models.BooleanField()
    is_hybrid=models.BooleanField()
    is_petrol=models.BooleanField()
    seo_name=models.CharField()
    is_newly_launched=models.BooleanField()
    default_variant=models.CharField()
    variant_featurs=models.ManyToManyField()
    url=models.CharField()
    image=models.ImageField()
    video=models.ManyToManyField()
    description=models.CharField()
    launched_on=models.CharField()
    prons=models.CharField()
    cons=models.CharField()
    introduction=models.CharField()
    styling_and_quality=models.CharField()
    ergonomics_and_comfort=models.CharField()
    performance_and_handling=models.CharField()
    features_and_technology=models.CharField()
    fuel_efficiency=models.CharField()

    
   
class VariantFeature(BaseModel):
    name = models.CharField()
    description = models.TextField()
    created_by = models.CharField(max_length=255)
    modified_by = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    
class ContactUs(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.subject
    
    
    
class BaseModel(BaseModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.PositiveIntegerField()
    updated_by = models.PositiveIntegerField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete_instance(self):
        self.is_deleted = True
        self.save()
        
class PriceSpecification(BaseModel):
    bike_variant = models.ForeignKey(BikeVariant, on_delete=models.CASCADE)
    price_exshow_room = models.DecimalField(max_digits=10, decimal_places=2)
    price_label_color = models.CharField(max_length=255)
    price_suffix = models.CharField(max_length=255)
    price_status = models.CharField(max_length=255)
    is_newly_launched = models.BooleanField(default=False)
    default_variant = models.BooleanField(default=False)
    variant_features = models.ManyToManyField('VariantFeature')
    created_by = models.CharField(max_length=255)
    modified_by = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
 

class Image(BaseModel):
    name = models.CharField(max_length=200)
    file = models.ImageField(upload_to='images/')
    def _str_(self):
        return self.name
    
    

