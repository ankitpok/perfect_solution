from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Booking, Service, Review

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'id_booking_date'}),
        input_formats=['%m/%d/%Y']
    )

    class Meta:
        model = Booking
        fields = ['booking_date']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'review_text', 'rating']
        
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],  # 1 to 5 ratings
        widget=forms.RadioSelect,
        required=True,
    )

        
