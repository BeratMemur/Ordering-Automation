from django.shortcuts import get_object_or_404, redirect, render
from products.forms import ProductCreateForm, UploadForm
from .models import Product, Category, UploadModel

def index(request):
    product = Product.objects.all().order_by("price")
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

def getProductsByCategory(request, slug):
    product = Product.objects.filter(categories__slug = slug).order_by("price")
    category = Category.objects.all()

    return render(request, 'products/index.html', {
        'product': product,
        'category': category,
        'activeCategory': slug,
    })

def create_product(request):
    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/urunler")
    else:
        form = ProductCreateForm()
    return render(request, "products/create-product.html", {"form": form})

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image = request.FILES["image"])
            model.save()
            return render(request, "products/success.html")
    else:
        form = UploadForm()
    return render(request, "products/upload.html", {"form":form})

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        product = Product.objects.filter(name__contains=q)
        category = Category.objects.all()
    else:
        redirect('products/index.html')

    return render(request, 'products/list.html', {
        'product': product,
        'category': category,
    })

