# from django.db import models

# # Create your models here.

# class Customer(models.Model):
#     username=models.CharField()
#     fullname=models.CharField()
#     email=models.EmailField(unique=True)
#     password=models.CharField(max_length=20)

    

# class Destination(models.Model):
#     destinaion=models.CharField(max_length=100)
#     image=models.ImageField()
#     trips=models.IntegerField(default=0)


# class TourCategory(models.Model):
#     name=models.CharField(max_length=100)
#     duration=models.CharField(max_length=100)
#     tourType=models.CharField(max_length=100)
#     groupSize=models.CharField(max_length=100)
#     cost=models.CharField(max_length=100)
#     customer=models.CharField(max_length=100)
#     infant_count=models.IntegerField()
#     children_count=models.IntegerField()
#     adult_count=models.IntegerField()
#     guests=models.CharField(max_length=100)
#     images=models.ImageField()
#     description=models.TextField()
#     highlights=models.TextField()
#     inclusives=models.TextField()
#     exclusives=models.TextField()
#     tour_location=models.CharField(max_length=100)
#     is_favourite=models.BooleanField(default=False)
#     date=models.DateField()
#     language=models.CharField(max_length=100)
#     destination=models.CharField(max_length=100)