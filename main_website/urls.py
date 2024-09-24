from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('index.html', views.homepage, name="home"),
    path('shop-listing.html', views.shoplist, name='shoplist'),
    path('shop-detail.html/<int:service_id>/', views.shopdetail, name='shopdetail'),
]