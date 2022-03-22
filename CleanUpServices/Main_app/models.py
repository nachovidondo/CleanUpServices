from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images_uploaded',null=True, blank=True)
    description = models.TextField()
    video  = models.FileField(upload_to='videos_uploaded',null=True,blank=True)
    
    def __str__(self):
        return self.name
    


class Happy_Customer(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images_uploaded',null=True, blank=True)
    description = models.TextField()
 
    def __str__(self):
        return self.name
    
class Plan(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    def __str__(self):
        return self.name
    
class Features(models.Model):
    name = models.CharField(max_length=200)
    plan  = models.ForeignKey(Plan, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    name = models.CharField(max_length=200, default="--")
    image = models.ImageField(upload_to="Portfolio_images")
    
    def __str__(self):
            return str(self.image)
    