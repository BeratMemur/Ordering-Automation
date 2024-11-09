from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Product, Category

def index(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'products/index.html',{
        'product': product,
        'category': category,
    })

def details(request, slug):
    product = get_object_or_404(Product, slug = slug)
    context = {
        'product': product,
    }
    return render(request, 'products/details.html', context)

def getProductsDetailsByCategory(request, slug):
    product = Product.objects.filter(categories__slug = slug)
    category = Category.objects.all()

    return render(request, 'products/index.html', {
        'product': product,
        'category': category,
        'activeCategory': slug,
    })