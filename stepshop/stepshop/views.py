from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


def get_basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    return basket


def index(request):
    title = 'Stepshop'

    products = Product.objects.all()  # [:4]

    context = {
        'title': title,
        'products': products,
        'basket': get_basket(request),
    }

    return render(request, 'stepshop/index.html', context=context)


def contacts(request):
    title = 'Contacts'

    context = {
        'title': title,
        'basket': get_basket(request),
    }
    return render(request, 'stepshop/contact.html', context)


def about(request):
    title = 'About us'

    context = {
        'title': title,
        'basket': get_basket(request),
    }
    return render(request, 'stepshop/about.html', context)
