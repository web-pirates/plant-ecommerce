from django.shortcuts import render, redirect
from captcha.image import ImageCaptcha

from .forms import Product

# Create your views here.
def index(request):
	return render(request, 'shop/index.html')


def dbform(request):
	return render(request, 'shop/dbform.html')

def scategory(request):
	return render(request, 'shop/scategory.html')

def pdetail(request):
	return render(request, 'shop/pdetail.html')

def pcheckout(request):
	return render(request, 'shop/pcheckout.html')

def shoppingcart(request):
	return render(request, 'shop/shoppingcart.html')

def confirmation(request):
	return render(request, 'shop/confirmation.html')

def product_detail(request):
	pass

