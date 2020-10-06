from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# Create your views here.
from .models import *
from django.core.mail import send_mail



def store(request):
    home = Home.objects.all()
    return render(request, 'store/store.html',{'home': home} )


def checkout(request):
    checkouts = ShippingAddress.objects.all()
    '''
    send_mail('saree orderr',
    '{{checkout.customer_name}},{{checkout.address}},{{checkout.city}},{{checkout.state}},{{checkout.zipcode}},{{checkout.date_added}},{{checkout.phone_number}},{{checkout.payment}},{{checkout.name}},{{checkout.price}},{{checkout.image}}',
    'pendem.svs@gmail.com', 
    ['srinivaspendem2612@gmail.com'],fail_silently=False
    )
    '''
    '''
    customer_name = request.POST["customer_name"]
    email = request.POST["address"]
    address = request.POST["address"]
    city = request.POST["city"]
    State = request.POST["state"]
    zipcode = request.POST["zipcode"]
    phone_number = request.POST["phone_number"]
    payment = request.POST["payment"]
    
    shippingaddress= ShippingAddress(customer_name=customer_name, email=email, address=address, city=city, State=State, zipcode=zipcode, phone_number=phone_number, payment=payment)
    shippingaddress.save()

    '''
    return render(request, 'store/checkout.html',{'checkouts':checkouts} )


def product(request):
    products = Product.objects.all()
    return render(request, 'store/product.html', {'products': products})
