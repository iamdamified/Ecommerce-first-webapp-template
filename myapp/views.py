from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product, Subscriber, Contact
from .forms import ContactForm

# Create your views here.

def home_page(request):

    if request.method == "GET":
        all_categories = Category.objects.all()
        # mens_products = Product.objects.filter(category=2) # A foreignKey called in model for category uses id and not the English name given to the choices as done in Category class
        mens_products = Product.objects.filter(category__name="MEN") # This helps the database to recognize and use the Instance name and not its default ID
        womens_products = Product.objects.filter(category__name="WOMEN")
        kids_products = Product.objects.filter(category__name="kids")

        context = {
            'all_categories': all_categories,
            'mens_product': mens_products,
            'womens_product': womens_products,
            'kids_product': kids_products

        }
    # Bound instance
    elif request.method == "POST":
        #  NOTE The name and email we have in the bracket in quotes is pointing to the name and email in quote in the form
        new_subscribers_name = request.POST["name"] # OR request.POST.get("name")
        new_subscribers_email = request.POST("email") # OR request.POST.get["email"]
        # The below is the ORM that describes what operation the application does with the data received from the user throught the form.
        Subscriber.objects.create(name=new_subscribers_name, email=new_subscribers_email)
        # The below describes what the form reaction would be after submiting
        # return HttpResponse("You have subscribed sucessfully")
        return redirect("productslink")
    
    return render(request, "myapp/index.html", context)


# Learn more about SENDGRID on twilo.com to know how to distribute newsletters to emails collected from this form (twilo.com/blog/email-activation-django-sendgrid)


def contact(request):
    # Unbound instance
    if request.method == "GET":
        form = ContactForm()
    # Bound instance
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()# This only is needed for second Method the below is not needed before return
            # contact_name = form.cleaned_data["name"]
            # contact_email = form.cleaned_data["email"]
            # contact_subject = form.cleaned_data["subject"]
            # contact_message = form.cleaned_data["message"]

            # Contact.objects.create(name=contact_name, email=contact_email, subject=contact_subject, message=contact_message)
            return HttpResponse("You have submitted your contact")
    context = {
        "form": form
    }
        
    return render(request, "myapp/contact2.html", context)




def contact_page(request):
    return render(request, "myapp/contact.html")

def about_page(request):
    return render(request, "myapp/about.html")

def products_page(request):
    return render(request, "myapp/products.html")

def singleproduct_page(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'oneproduct': product
    }
    return render(request, "myapp/single-product.html", context)
