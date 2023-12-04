from django.db import models

# Create your models here.


from django.db import models



class CarModel(models.Model):
    Condition = models.IntegerField(blank=True,null=True)
    Vehicle_brand = models.IntegerField(blank=True,null=True)
    Production_year = models.IntegerField(blank=True,null=True)
    Mileage_km = models.IntegerField(blank=True,null=True)
    Power_HP = models.IntegerField(blank=True,null=True)
    Displacement_cm3 = models.IntegerField(blank=True,null=True)
    Fuel_type = models.IntegerField(blank=True,null=True)
    Transmission = models.IntegerField(blank=True,null=True)
    Type = models.IntegerField(blank=True,null=True)
    Doors_number = models.IntegerField(blank=True,null=True)
    Colour = models.IntegerField(blank=True,null=True)
    First_owner = models.IntegerField(blank=True,null=True)
    FT = models.IntegerField(blank=True,null=True)
    Price = models.IntegerField(blank=True,null=True)

    def __str__(self) -> str:
        return str(self.Price)

        





class Item(models.Model):

   

    age = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=100,blank=True,null=True)
    item = models.CharField(max_length=100,blank=True,null=True)
    category = models.CharField(max_length=100,blank=True,null=True)
  
    amount = models.IntegerField(blank=True,null=True)
    prev_purc = models.IntegerField(blank=True,null=True)
    rating = models.DecimalField(max_digits=6,decimal_places=6,blank=True,null=True)
    
    location = models.CharField(max_length=100,blank=True,null=True)
    size = models.CharField(max_length=100,blank=True,null=True)
    color = models.CharField(max_length=100,blank=True,null=True)
    season = models.CharField(max_length=100,blank=True,null=True)
    
    subscribed = models.CharField(max_length=100,blank=True,null=True)
    pay_meth = models.CharField(max_length=100,blank=True,null=True)
    
    shipping_type = models.CharField(max_length=100,blank=True,null=True)
    discount = models.CharField(max_length=100,blank=True,null=True)
    promo = models.CharField(max_length=100,blank=True,null=True)
    pref_pay_meth = models.CharField(max_length=100,blank=True,null=True)
    frequency = models.CharField(max_length=100,blank=True,null=True)
    
    
    def __str__(self) -> str:
        return str(self.item)

        