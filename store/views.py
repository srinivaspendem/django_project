from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.db.models import Q
# Create your views here.
from .models import *
from django.core.mail import send_mail



def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)


def product(request, pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    context = {'products':products,'product':product}
    return render(request, 'store/product.html', context)



def checkout(request, pk):
	product = Product.objects.get(id=pk)
	products = Product.objects.all()
	adress = ShippingAddress.objects.all()
	context = {'products':products,'adress':adress,'product':product}
	return render(request, 'store/checkout.html', context)




def processOrder(request): 
	order = Order.objects.get
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = ShippingAddress(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'store/check.html',context)
	# full_name = request.POST["full_name"]
	# email = request.POST["email"]
	# address = request.POST["address"]
	# city = request.POST["city"]
	# state = request.POST["state"]
	# zipcode = request.POST["zipcode"]
	# phone = request.POST["phone"]
	# payment_method = request.POST["payment_method"]
	
	# shipping_address = ShippingAddress(full_name=full_name,email=email,address=address,city=city,state=state,zipcode=zipcode,phone=phone,payment_method=payment_method)
	# shipping_address.save()

	# return render(request, 'store/checkout.html')

	# transaction_id = datetime.datetime.now().timestamp()
	# data = json.loads(request.body)

def createpost(request):
	
	if request.method == 'POST':
		if request.POST.get('full_name') and request.POST.get('email') and request.POST.get('address') and request.POST.get('city') and request.POST.get('state') and request.POST.get('zipcode') and request.POST.get('phone') and request.POST.get('payment_method') and request.POST.get('date_added'):
			post=ShippingAddress()
			post.full_name= request.POST.get('full_name')
			post.email= request.POST.get('email')
			post.address= request.POST.get('address')
			post.city= request.POST.get('city')
			post.state= request.POST.get('state')
			post.zipcode= request.POST.get('zipcode')
			post.phone= request.POST.get('phone')
			post.payment_method= request.POST.get('payment_method')
			post.date_added= request.POST.get('date_added')
			post.save()
			return render(request, 'store/check.html')
	else:
		return render(request,'store/check.html')
	

				

def search(request):
	




	query = request.GET.get('q')
	keywords = query.split(" ")
	final_query=None
	for keyword in keywords:
		current_query=Q(description__contains=keyword) | Q(name__contains=keyword)
		if final_query is None:
			final_query = current_query
		else:
			final_query = final_query | current_query

	products = Product.objects.filter(final_query)
	context = {'products':products }

			
	return render(request,'store/search.html', context)








# def get_queryset(self): 
# 	queryset = []
# 	keywords = query.split(" ")
# 	for q in queries:
# 		post =Product.objects.filter(
# 			Q(description__icontains=keywords[0])|
# 			Q(name__icontains=keywords[0])|
		

#         ).distinct()
# 		for post in posts:
# 			queryset.append(post) 
# 		return list(set(queryset))

		  
# if request.POST['submit']=='Add':

