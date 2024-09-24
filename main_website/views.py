from django.shortcuts import render
from bookings.models import Service as serv
from bookings.models import Categories as cats

def homepage(request):
    services = serv.objects.all()
    return render(request, 'index.html', {'services': services})

def shoplist(request):
    return render(request, 'shop-listing.html')

def shopdetail(request, service_id):
    services = serv.objects.get(id=service_id)
    categories = services.categories_set.all()
    return render(request, 'shop-detail.html', {'services': services, 'service_id': service_id,'categories':categories})

