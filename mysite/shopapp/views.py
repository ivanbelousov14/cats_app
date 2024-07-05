from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from timeit import default_timer


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