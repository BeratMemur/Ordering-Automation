from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'products/index.html')

def getProductsByCategory(request, category):
    return HttpResponse(f"{category} listesi")