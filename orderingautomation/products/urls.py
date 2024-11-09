from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.details, name="product_details"),
    path('category/<slug:slug>', views.getProductsDetailsByCategory, name='products_details_by_category'),
]
