from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect # inserted this line
from django.apps import apps

for key in apps.get_app_config('products').models:
    print key

def index(request):

	test = apps.get_app_config('products').models['cart'].apps.get_app_config('products').models['User'].objects.filter(id=1)
	print test
	context = Cart.User.objects.filter(id = 1)
	return render(request, 'cart/index.html', context) # updated this line

def add_to_cart(request):
	products = apps.get_app_config('products').models['product']
	users = apps.get_app_config('products').models['user']
	cart = apps.get_app_config('products').models['cart']
	

	user = users.objects.get(id=1)
	product = products.objects.get(id=request.POST['id'])
	entry = cart(user=user, product=product, qty=request.POST['qty'])
	entry.save()
	return redirect('/')

def remove_from_cart(request):
	products = apps.get_app_config('products').models['product']
	users = apps.get_app_config('products').models['user']
	cart = apps.get_app_config('products').models['cart']

	user = users.objects.filter(id=1)
	product = products.objects.filter(id=request.post['id'])
	item = cart.filter(user=user, product = product)
	item.delete()