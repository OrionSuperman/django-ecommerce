from django.http import HttpResponse, Http404
from django.shortcuts import render # inserted this line
from .models import User, Product, Cart
def index(request):
	items = Product.objects.all()
	cart = Cart.objects.all()


	return render(request, 'products/index.html', {'items':items, 'cart':cart}) # updated this line 



