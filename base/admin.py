from django.contrib import admin
from . import models


# Register your models here.


class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "duration", "cost", "tour_location", "country")


class CountrySafariAdmin(admin.ModelAdmin):
    list_display = ("country_name",)


class TourImageAdmin(admin.ModelAdmin):
    list_display = ("tour",)


class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "note")

class VisaAdmin(admin.ModelAdmin):
    list_display=("id","first_name","last_name","email")


admin.site.register(models.TourCategory, TourCategoryAdmin)
admin.site.register(models.CountrySafari, CountrySafariAdmin)
admin.site.register(models.TourImage, TourImageAdmin)
admin.site.register(models.Enquiry, EnquiryAdmin)
admin.site.register(models.Visa,VisaAdmin)
