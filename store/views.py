from django.shortcuts import render
from .models.product import Product

# Create your views here.

def index(request):

    prds = Product.objects.all()
    # print(prds)

    return render(request, "index.html", {'products' : prds})