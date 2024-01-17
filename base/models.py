from django.db import models
from django.contrib.auth.models import User
# # Create your models here.

# class Customer(models.Model):
#     username=models.CharField()
#     fullname=models.CharField()
#     email=models.EmailField(unique=True)
#     password=models.CharField(max_length=20)

class TripCategory(models.Model):
    name=models.CharField(max_length=100)

# class Destination(models.Model):
#     destinaion=models.CharField(max_length=100)
#     image=models.ImageField()
#     trips=models.IntegerField(default=0)

class CountrySafari(models.Model):
    country_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images",blank=True,null=True)

    def __str__(self) -> str:
        return self.country_name


class TourCategory(models.Model):
    name=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    cost=models.CharField(max_length=100)
    description=models.TextField()
    inclusives=models.TextField(blank=True,null=True)
    exclusives=models.TextField(blank=True,null=True)
    tour_location=models.CharField(max_length=100,null=True,blank=True)
    destination=models.CharField(max_length=100,null=True,blank=True)
    country=models.ForeignKey(CountrySafari,on_delete=models.DO_NOTHING,blank=True,null=True)
    image=models.ImageField(upload_to="tour_images",blank=True,null=True)
    highlights=models.TextField(blank=True,null=True)
    groupSize=models.CharField(max_length=100,blank=True,null=True)
    languages=models.CharField(max_length=50,default="English")
    # tourType=models.CharField(max_length=100)
    
    # customer=models.CharField(max_length=100)
    # infant_count=models.IntegerField()
    # children_count=models.IntegerField()
    # adult_count=models.IntegerField()
    # guests=models.CharField(max_length=100)
    # images=models.ImageField()
    # highlights=models.TextField()
    # is_favourite=models.BooleanField(default=False)
    # date=models.DateField(auto/)
    # language=models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.id)

class TourImage(models.Model):
    image=models.ImageField(upload_to="tour_images")
    tour=models.ForeignKey(TourCategory,on_delete=models.DO_NOTHING)


class Enquiry(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=30)
    email=models.EmailField()
    note=models.TextField(max_length=500)


class Payment(models.Model):
    reference = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')

class Cart(models.Model):
    trips = models.ManyToManyField(TourCategory)
    total=models.DecimalField(max_digits=10,decimal_places=2,default=0.0)

class Booking(models.Model):
    trip=models.ForeignKey(TourCategory,on_delete=models.DO_NOTHING),
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING),
    reference=models.CharField(max_length=20)
    amount=models.DecimalField(decimal_places=2,max_digits=5)


class Visa(models.Model):
    CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]

    first_name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    date_of_birth=models.DateField()
    country_of_origin=models.CharField(max_length=100)
    city_of_origin=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    passport_number=models.CharField(max_length=100)
    passport_issue_date=models.DateField()
    passport_expiry_date=models.DateField()
    email2=models.EmailField()
    phone=models.CharField(max_length=20)
    reason_for_travel=models.TextField()
    proposed_day_of_arrival=models.DateField()
    departure_date=models.DateField()
    home_address=models.CharField(max_length=100)
    address_in_kenya=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    previous_entry=models.CharField(max_length=3, choices=CHOICES)
    conviction=models.CharField(max_length=3, choices=CHOICES)

    passport_image=models.ImageField(upload_to="visa_docs")
    passport_data_page=models.FileField(upload_to="visa_docs")
    passport_front_cover=models.FileField(upload_to="visa_docs")
    invitation_letter=models.FileField(upload_to="visa_docs")
    aknowledge=models.BooleanField()
    declaration=models.BooleanField()


class  BoookingPayments(models.Model):
	tour = models.ForeignKey(TourCategory,on_delete=models.DO_NOTHING,null=True,blank=True)
	user=models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True)
	amount = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	date=models.DateTimeField(auto_now_add=True)
	reference = models.CharField(max_length=10,null=True,blank=True)
	payment_method=models.CharField(max_length=100,null=True,blank=True)
	confirmation_code = models.CharField(max_length=100,null=True,blank=True)
	payment_status_description=models.CharField(max_length=100,null=True,blank=True)
	payment_account = models.CharField(max_length=50,null=True,blank=True)
	merchant_reference=models.CharField(max_length=100,null=True,blank=True)
	currency=models.CharField(max_length=100,null=True,blank=True)
	order_tracking_id=models.CharField(max_length=100,null=True,blank=True)
	create_date=models.DateTimeField(null=True,blank=True)
	message=models.CharField(max_length=100,blank=True,null=True)
	status_code=models.CharField(max_length=20,blank=True,null=True)
	payment_status_code = models.CharField(max_length=20,null=True,blank=True)
	status = models.CharField(max_length=20,null=True,blank=True)
 
	