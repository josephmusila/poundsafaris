import json
import math
from django.utils import timezone
# from datetime import *
import uuid
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
from . import models
from django.db.models import Q
from .forms import LoginForm, RegisterForm, EnquiryForm, VisaForm, TourCategoryForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
import ast
from django.core.paginator import Paginator
import requests
import json
import http.client
import asyncio
from django.http import JsonResponse
import httpx
from django.urls import reverse

# from django_pesapal.views import PaymentRequestMixin
# Create your views here.


PESAPAL_CONSUMER_KEY = 'INVBqKBsmVnVgdHiIYyqpJxSNIkNHp/K'
PESAPAL_CONSUMER_SECRET = 'yRiA3QOS2pdzkoPfAAHAv3BOB+o='
PESAPAL_CALLBACK_URL = 'YOUR_CALLBACK_URL'


# class PaymentView(PaymentRequestMixin):

#     def get_pesapal_payment_iframe(self):

#         '''
#         Authenticates with pesapal to get the payment iframe src
#         '''
#         order_info = {
#             'first_name': 'Some',
#             'last_name': 'User',
#             'amount': 1,
#             'description': 'Payment for X',
#             'reference': 2,  # some object id
#             'email': 'josemusila03@gmail.com',
#         }

#         iframe_src_url = self.get_payment_url(**order_info)
#         return iframe_src_url


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'base/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'base/register.html', {'form': form})


def sign_in(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'base/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(
                    request, f'Hi {username.title()}, welcome back!')
                print("Authenticated")
                return redirect('home')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        print("Not Authenticated")
        return render(request, 'base/login.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('home')


def index(request):

    name = request.GET.get("name") if request.GET.get('name') != None else ''
    duration = request.GET.get("duration") if request.GET.get(
        'duration') != None else ''
    group = request.GET.get("group") if request.GET.get(
        'group') != None else ''
    searched_trips = models.TourCategory.objects.filter(
        Q(name__icontains=name) |
        Q(duration=duration) |
        Q(description=group)
    )

    # trending_tours=range(0,3)
    clients_count = range(0, 3)
    trending_tours = models.TourCategory.objects.all()[:6]
    country_trips = models.CountrySafari.objects.all()
    kenya_trips_count = models.TourCategory.objects.filter(country=1).count()
    uganda_trips_count = models.TourCategory.objects.filter(country=2).count()
    tanzania_trips_count = models.TourCategory.objects.filter(
        country=3).count()
    trending = models.TourCategory.objects.all()[:3]

    searched_trip_ids = []
    cart = models.Cart.objects.all()
    cart_count=cart.count()

    request.session['count'] = cart_count
    # request.session['cart'] = cart

    for item in searched_trips:
        searched_trip_ids.append(item.id)

    # print(searched_trip_ids)
    for tour in trending_tours:
        trip = getCountryTrips(tour.country)

    serialized_data = json.dumps(
        list(trending_tours.values("name")), cls=DjangoJSONEncoder)

    return render(request, 'base/index.html', context={
        "trending_tours": trending_tours,
        "clients_count": clients_count,
        "country_trips": country_trips,
        "kenya_trips_count": kenya_trips_count,
        "uganda_trips_count": uganda_trips_count,
        "tanzania_trips_count": tanzania_trips_count,
        "trending": trending,
        "searched_trips": searched_trip_ids,
        'serialized_data': serialized_data,
        "cart":cart,
        "cart_count":cart_count

    })


def tourPage(request, pk=None):
    tour = models.TourCategory.objects.get(id=pk)
    images = models.TourImage.objects.filter(tour=pk)
    trending = models.TourCategory.objects.all().order_by('?')[:3]
    # print(trending.count())
    image_count = range(0, 3)
    cart_count = 0
    form = EnquiryForm()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Message Sent Succesfully')
            # return HttpResponse('Form submitted successfully!')
    else:
        form = EnquiryForm()
    context = {
        "tour": tour,
        "images": images,
        "image_count": image_count,
        "form": form,
        "cart_count": cart_count,
        "trending": trending
    }
    return render(request, "base/tour_item.html", context)


def searchPage(request):
    searched_trips = request.GET.get("searched_trips", None)
    try:
        my_list = ast.literal_eval(searched_trips)
        print(my_list[0])
    except (SyntaxError, ValueError):
        print("Invalid string representation for a list.")

    context = {
        "searched_trips": searched_trips
    }
    return render(request, "base/searched_trips.html", context)


def enquiry(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        note = request.POST.get("note")
    else:
        form = EnquiryForm()

    return redirect(request, 'base/home.html')

def addToCart(request,trip_id):
    trip=models.TourCategory.objects.get(id=trip_id)
    cart_entry=models.Cart.objects.create()
    # cartItem,created = models.Cart.objects.get_or_create(item=trip)
    cart_entry.item.set([trip])
    cart_entry.save()

    cart_items=[]
    # cart_items.append(trip)
    # print(len(cart_items))
    cart_count= models.Cart.objects.all()
    print(cart_count.count())

    return redirect('home')

def booking(request, user_id, ):
    # trip = models.TourCategory.objects.get(id=trip_id)
    user = User.objects.get(id=user_id)
    cart_items = models.Cart.objects.all()
    print(cart_items.count( ))

    context = {
        "trips": cart_items,
        "user": user
    }
    return render(request, 'base/booking.html', context)


def getCountryTrips(country_name):
    country_Trip = models.TourCategory.objects.filter(
        Q(country__country_name=country_name))
    return country_Trip


def visaPage(request):
    if request.method == 'POST':
        form = VisaForm(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
            messages.success(request, f'Visa Form Data Sent Succesfully')
            return redirect('home')
            # return HttpResponse('Form submitted successfully!')
    else:
        print("form not saved")
        form = VisaForm()
    visaForm = VisaForm()
    context = {
        "visa_form": visaForm
    }
    return render(request, "base/visa.html", context)


def aboutPage(request):
    return render(request, "base/about_us.html")


def kenyasafari(request):
    kenya_safari = models.TourCategory.objects.filter(country=1)
    safari_count = range(0, 6)

    return render(request, "base/kenya_safaris.html", context={
        "safari_count": safari_count,
        "tours": kenya_safari

    })


def tanzaniasafari(request):
    tanzania_safari = models.TourCategory.objects.filter(country=3)
    safari_count = range(0, 6)
    return render(request, "base/tanzania_safaris.html", context={
        "safari_count": safari_count,
        "tours": tanzania_safari
    })


def ugandasafari(request):
    uganda_safari = models.TourCategory.objects.filter(country=2)
    safari_count = range(0, 6)
    return render(request, "base/uganda_safaris.html", context={
        "safari_count": safari_count,
        "tours": uganda_safari
    })


def rwandasafari(request):
    safari_count = range(0, 6)
    return render(request, "base/rwanda_safaris.html", context={
        "safari_count": safari_count
    })


def christmasdeals(request):
    return render(request, "base/christmas_deals.html")


def contacts(request):
    return render(request, "base/contacts.html")


def blogs(request):
    return render(request, "base/blogs.html")


# footer pages

def affiliate(request):
    return render(request, "base/footer_pages/affiliate.html")


def legal(request):
    return render(request, "base/footer_pages/legal.html")


def policy(request):
    return render(request, "base/footer_pages/policy.html")


def rewards(request):
    return render(request, "base/footer_pages/rewards.html")


def team(request):
    return render(request, "base/footer_pages/team.html")


def workWithUs(request):
    return render(request, "base/footer_pages/work.html")


def careers(request):
    return render(request, "base/footer_pages/careers.html")


# admin


def dashboard(request):
    return render(request, "base/admin/home.html")


def dashboardTrips(request):
    trips = models.TourCategory.objects.all()
    paginator = Paginator(trips, 5)
    number_of_pages = math.ceil(trips.count()/5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        "page_count": number_of_pages
    }
    return render(request, "base/admin/all_trips.html", context)


def addTour(request):
    page = "add-tour"
    form = TourCategoryForm()
    if request.method == "POST":
        form = TourCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard_trips")

    context = {
        "form": form,
        "page": page
    }

    return render(request, "base/admin/add_trip.html", context)


# payments

async def getAuthToken(request):
    url = "https://pay.pesapal.com/v3/api/Auth/RequestToken"
    payload = json.dumps({
        "consumer_key": "INVBqKBsmVnVgdHiIYyqpJxSNIkNHp/K",
        "consumer_secret": "yRiA3QOS2pdzkoPfAAHAv3BOB+o="
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': '__cf_bm=UkeRsH42trDKHeVZOlLjH_uLOmdQe8H_g3SBfPDyT44-1702363838-1-ATlP/7hc90zrXyGLz/go4//imcapHXvLOBhtK6LH1FEUsx3Ucx43KlmnAk/AE+uItRmmZFjktFP8VNmL5T91rB0='
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, data=payload)
        return response.json()


async def registerIpnUrl(request):
    try:
        data = await getAuthToken(request)
        token_value = data.get("token")
        url = "https://pay.pesapal.com/v3/api/URLSetup/RegisterIPN"
        payload = json.dumps({
            "url": "http://127.0.0.1:8000/ipn",
            "ipn_notification_type": "GET"
        })
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer  {token_value}',
            'Cookie': '__cf_bm=D6i0Q55cV0fAywZ6F2kYQPUc3BX0MVocklf0fNmAqhI-1702362813-1-AbM3loCbxQuLR18vRIpouqS9JX1CU/bZP17xcrk5+SQYgT1paOY3e3FDh3UFIb3mmKPaIXWlTMGbFmJWrZEMMdA='
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, data=payload)
        return JsonResponse({'status': 'Data received successfully'})
    except Exception as e:
        print(f"Error fetching data: {e}")
        return JsonResponse({'status': 'Error fetching data'}, status=500)
    return HttpResponse("Hello World")


async def submitOreder(request):
    try:
        data = await getAuthToken(request)
        token_value = data.get("token")
        url = "https://pay.pesapal.com/v3/api/Transactions/SubmitOrderRequest"
        callback_url=reverse("home")

        payload = json.dumps({
            "id":  "12345667778",
            "currency": "KES",
            "amount": 1,
            "description": "Payment description goes here",
            "callback_url": callback_url,
            "redirect_mode": "",
            "notification_id": "0c16ff0c-45bc-432a-9dd2-ddd6986c93d0",
            "branch": "Mega Stores Kenya",
            "billing_address": {
                "email_address": "josemusila03@gmail.com",
                "phone_number": "0745787487",
                "country_code": "KE",
                "first_name": "Joseph",
                "middle_name": "Jela",
                "last_name": "Musila",
                "line_1": "Pesapal Limited",
                "line_2": "",
                "city": "",
                "state": "",
                "postal_code": "",
                "zip_code": ""
            }
        })
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token_value}',
            'Cookie': '__cf_bm=UkeRsH42trDKHeVZOlLjH_uLOmdQe8H_g3SBfPDyT44-1702363838-1-ATlP/7hc90zrXyGLz/go4//imcapHXvLOBhtK6LH1FEUsx3Ucx43KlmnAk/AE+uItRmmZFjktFP8VNmL5T91rB0='
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, data=payload)

        json_response = response.json()
        redirect_url = json_response.get("redirect_url")
        print(response.content)
        return redirect(redirect_url)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return JsonResponse({'status': 'Error fetching data'}, status=500)
