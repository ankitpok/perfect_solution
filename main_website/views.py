from django.shortcuts import render, redirect
from bookings.models import Service as serv, Category as cats, SliderImage as img, Review as rev
from django.http import JsonResponse
from bookings.forms import ReviewForm
from django.contrib.auth.decorators import login_required

def homepage(request):
    services = serv.objects.all()
    slider = img.objects.all()
    form = ReviewForm()
    reviews = rev.objects.all()
    return render(request, 'index.html', {
        'services': services,
        'slider': slider,
        'reviews': reviews,
        'form': form,
    })

def shoplist(request):
    return render(request, 'shop-listing.html')

def shopdetail(request, service_id):
    service = serv.objects.get(id=service_id)
    categories = cats.objects.filter(service = service) 
    return render(request, 'shop-detail.html', {
        'service': service,
        'categories': categories
    })
    
def category(request, category_id):
    category = cats.objects.get(id=category_id)
    service = category.service 
    service_id = category.service.id
    
    return render(request, 'category_detail.html', {
        'category': category,       
        'service': service,
        'service_id':service_id,         
    })

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return JsonResponse({
                'status': 'success',
                'review': {
                    'user_name': review.user_name,
                    'review_text': review.review_text,
                    'rating': review.rounded_rating(),
                    'created_at': review.created_at.strftime('%Y-%m-%d %H:%M:%S')
                }
            })
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
        
