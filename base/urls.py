from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="home"),
    path("tour_item/<str:pk>",views.tourPage,name="details"),
    path("visa",views.visaPage,name="visa"),
    path("about",views.aboutPage,name="about"),
    path("kenya_safaris",views.kenyasafari,name="kenya_safaris"),
    path("uganda_safaris",views.ugandasafari,name="uganda_safaris"),
    path("tanzania_safaris",views.tanzaniasafari,name="tanzania_safaris"),
    path("rwanda_safaris",views.rwandasafari,name="rwanda_safaris"),
    path("christmas_deals",views.christmasdeals,name="christmas_deals"),
    path("contacts",views.contacts,name="contacts"),
    path("search",views.searchPage,name="search"),
    path("blogs",views.blogs,name="blogs"),
    path("booking/<str:user_id>/<str:pk>/",views.booking,name="booking"),

    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),

    path('enquiry/',views.enquiry,name="enquiry"),

    # payments
 
   
]