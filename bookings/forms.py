from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Booking, Service

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# forms.py
from django import forms
from .models import Booking

# forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'id_booking_date'}),
        input_formats=['%m/%d/%Y']
    )

    class Meta:
        model = Booking
        fields = ['booking_date']


# class ServiceForm(forms.ModelForm):
#     class Meta:
#         model = Service
#         fields = ['name', 'description', 'price', 'duration', 'category', 'image']
        