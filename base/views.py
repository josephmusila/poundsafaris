from django.shortcuts import render

# Create your views here.

def index(request):

    trending_tours=range(0,3)
    clients_count=range(0,3)

    return render(request,'base/index.html',context={
        "trending_tours":trending_tours,
        "clients_count":clients_count

    })

def visaPage(request):
    return render(request,"base/visa.html")


def aboutPage(request):
    return render(request,"base/about_us.html")


def kenyasafari(request):
    safari_count=range(0,6)
    return render(request,"base/kenya_safaris.html",context={
        "safari_count":safari_count
    })

def tanzaniasafari(request):
    safari_count=range(0,6)
    return render(request,"base/tanzania_safaris.html",context={
        "safari_count":safari_count
    })

def ugandasafari(request):
    safari_count=range(0,6)
    return render(request,"base/uganda_safaris.html",context={
        "safari_count":safari_count
    })

def rwandasafari(request):
    safari_count=range(0,6)
    return render(request,"base/rwanda_safaris.html",context={
        "safari_count":safari_count
    })


def christmasdeals(request):
    return render(request,"base/christmas_deals.html")


def contacts(request):
    return render(request,"base/contacts.html")
