from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, "myapp/index.html")

def contact_page(request):
    return render(request, "myapp/contact.html")

def about_page(request):
    return render(request, "myapp/about.html")

def products_page(request):
    return render(request, "myapp/products.html")

def singleproduct_page(request):
    return render(request, "myapp/single-product.html")
