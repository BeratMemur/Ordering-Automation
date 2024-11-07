from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<category>', views.getProductsByCategory, name='products_by_category'),
]
