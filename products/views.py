from django.shortcuts import render
from .models import Product

def all_products(request):
    """ A view that will display all the products and allow search queries"""

    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)
