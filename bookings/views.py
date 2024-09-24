import base64
from datetime import datetime
import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from bookings.forms import LoginForm
from bookings.models import Service as serv
from .forms import *
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.timezone import make_aware


@login_required
def bookservice(request, service_id):
    service = Service.objects.get(id=service_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.service = service
            booking.booking_date = make_aware(datetime.strptime(form.cleaned_data['booking_date'].strftime('%Y-%m-%d'), '%Y-%m-%d'))
            booking.save()
            return redirect('bookings:esewarequest', booking_id=booking.id)
        else:
            print("form not valid") 
    else:
        form = BookingForm()
        print(form.errors)

    return render(request, 'book_service.html', {'service': service, 'form': form})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'booking_confirmation.html', {'booking': booking})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'index.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('book_service.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('book_service.html')

def esewarequest(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    service = booking.service
    total_amount = 100

    success_url = f'http://127.0.0.1:8000/bookings/booking_confirmation/{booking_id}'
    #success_url = request.build_absolute_uri(reverse('bookings:esewa_response', args=[booking_id]))

    context = {
        'booking_id': booking_id,
        'total_amount': total_amount,
        'success_url': success_url
    }
    if request.method == "POST":
        encoded_data = request.GET.get('data')
        if encoded_data:
            esewa_response(request,booking_id)
        else:
            print('failed')
            pass
        

    return render(request, 'esewarequest.html', context)

def esewa_response(request, booking_id):
    encoded_data = request.GET.get('data')
    if not encoded_data:
        return HttpResponse("Invalid response data", status=400)

    try:
        # Decode the base64-encoded data
        decoded_data = base64.b64decode(encoded_data).decode('utf-8')

        # Parse the JSON data
        response_data = json.loads(decoded_data)

        # Extract information
        transaction_code = response_data.get('transaction_code')
        status = response_data.get('status')
        total_amount = response_data.get('total_amount')
        transaction_uuid = response_data.get('transaction_uuid')
        product_code = response_data.get('product_code')

        # Log the response data (optional)
        print("Transaction Code:", transaction_code)
        print("Status:", status)
        print("Total Amount:", total_amount)
        print("Transaction UUID:", transaction_uuid)
        print("Product Code:", product_code)

        # Process the response data
        if status == "COMPLETE":
            # Update the booking status and mark as paid
            booking = get_object_or_404(Booking, id=booking_id)
            booking.booking_status = "Confirmed"
            booking.has_paid = True
            booking.save()
            # Redirect to the booking confirmation view
            return booking_confirmation(request,booking_id)
        else:
            return HttpResponse("Payment failed or incomplete", status=400)
    except Exception as e:
        print(f"Error processing eSewa response: {e}")
        return HttpResponse("Error processing response data", status=500)

    