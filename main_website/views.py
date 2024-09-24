from django.shortcuts import render
from bookings.models import Service as serv
from bookings.models import Categories as cats
from bookings.models import SliderImage as Slider

def homepage(request):
    services = serv.objects.all()
    slider = Slider.objects.all()
    return render(request, 'index.html', {'services': services, 'slider': slider})

def shoplist(request):
    return render(request, 'shop-listing.html')

def shopdetail(request, service_id):
    services = serv.objects.get(id=service_id)
    categories = services.categories_set.all()
    return render(request, 'shop-detail.html', {'services': services, 'service_id': service_id,'categories':categories})

