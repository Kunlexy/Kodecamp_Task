from django.db import models
# Create your models here.
class People(models.Model):
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    
        
    def __str__(self):
        return self.username

class Address(models.Model):
    user=models.OneToOneField(People, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.address

class Bio(models.Model):
    user=models.OneToOneField(People, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.bio


class Product(models.Model):
    product_name= models.CharField(max_length=100)
    product_price= models.CharField(max_length=15)
    product_cat = models.CharField(max_length=20)
    #postedby = models.ForeignKey(People, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.product_name

class Doctor(models.Model):
    fullname = models.CharField(max_length=100)
    speciality = models.CharField(max_length=50)
    hospital = models.CharField(max_length=50)
    patient = models.ForeignKey(People, on_delete = models.CASCADE)
    treatment = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.fullname 
   