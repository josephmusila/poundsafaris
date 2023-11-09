from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="home"),
    path("visa",views.visaPage,name="visa"),
    path("about",views.aboutPage,name="about"),
    path("kenya_safaris",views.kenyasafari,name="kenya_safaris"),
    path("uganda_safaris",views.ugandasafari,name="uganda_safaris"),
    path("tanzania_safaris",views.tanzaniasafari,name="tanzania_safaris"),
    path("rwanda_safaris",views.rwandasafari,name="rwanda_safaris"),
    path("christmas_deals",views.christmasdeals,name="christmas_deals"),
    path("contacts",views.contacts,name="contacts"),
    # path("christmas_deals",views.christmasdeals,name="christmas_deals")
   
]