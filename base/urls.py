from django.urls import path
from . import views
urlpatterns=[

    path("dashboard",views.dashboard,name="dashboard"),
    path("dashboard_trips",views.dashboardTrips,name="dashboard_trips"),
    path("add_tour",views.addTour,name="add_tour"),

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

    # booking
    path("booking/<str:tour_id>/",views.booking,name="booking"),
    path("addToCart/<str:trip_id>/",views.addToCart,name="addToCart"),

    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('profile/',views.profile,name="profile"),

    path('enquiry/',views.enquiry,name="enquiry"),

    # footer pages
    path('affiliate/',views.affiliate,name="affiliate"),
    path('legal/',views.legal,name="legal"),
    path('policy/',views.policy,name="policy"),
    path('rewards/',views.rewards,name="rewards"),
    path('team/',views.team,name="team"),
    path('work',views.workWithUs,name="work"),
    path('careers',views.careers,name="careers"),

    # payments
    path("getAuthToken",views.getAuthToken,name="getAuthToken"),
    path("registerIpnUrl",views.registerIpnUrl,name="registerIpnUrl"),
    path("submitOrder/<str:booking_id>",views.submitOreder,name="submitOrder"),
    path("transaction_status/<str:order_tracking_id>",views.getTransactionStatus,name="transactionStatus"),
 
   
]