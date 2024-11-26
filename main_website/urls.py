from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('add_review/', views.add_review, name='add_review'),
    path('shop-detail/<str:service_id>/', views.shopdetail, name='shopdetail'),
    path('category-detail/<str:category_id>/', views.category, name='category'),
]