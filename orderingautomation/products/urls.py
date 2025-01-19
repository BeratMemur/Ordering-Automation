from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('search', views.search, name="search"),
    path('create_product', views.create_product, name="create_product"),
    path('upload', views.upload, name='upload_image'),
    path('<slug:slug>', views.details, name="product_details"),
    path('category/<slug:slug>', views.getProductsByCategory, name='products_by_category'),
]
