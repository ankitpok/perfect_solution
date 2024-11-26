from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('<int:category_id>/', views.bookservice, name='bookservice'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('booking_confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('esewa-response/<int:booking_id>/', views.esewa_response, name='esewa-response'),
    path('esewarequest/<int:booking_id>/', views.esewarequest, name='esewarequest')
    
]