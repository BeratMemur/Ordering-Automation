from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    product = Product.objects.all()
    return render(request, 'products/index.html',{
        'product': product,
    })

def getProductsByCategory(request, category):
    return HttpResponse(f"{category} listesi")