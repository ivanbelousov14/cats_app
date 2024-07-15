from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from timeit import default_timer
from django.contrib.auth.models import Group
from shopapp.models import Product

def shop_index(request: HttpRequest):
    products = [
        ('laptop', 1290),
        ('laptop2', 12390),
        ('laptop', 12490),
        ('laptop', 12910),

    ]
    context = {
        "time_running": default_timer(),
        "products": products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)

def group_list(request: HttpRequest):
    context = {
        "groups": Group.objects.all(),

    }
    return render(request, 'shopapp/group_list.html', context=context)

def product_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),

    }
    return render(request, "shopapp/product_list.html", context=context)