from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product
from basketapp.models import Basket

from stepshop.views import get_basket


def products(request, pk=0):
    title = 'Products | Catalog'

    links_menu = ProductCategory.objects.all()
    products_all = Product.objects.all().order_by('price')

    context = {
        'title': title,
        'links_menu': links_menu,
        'products_all': products_all,
        'basket': get_basket(request),
    }

    # if pk is not None:
    if pk == 0:
        products_all = Product.objects.all().order_by('price')
        category = {'name': 'все', 'pk': 0}
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products_all = Product.objects.filter(category__pk=pk).order_by('price')

    context['category'] = category
    context['products_all'] = products_all

    return render(request=request, template_name='mainapp/products.html', context=context)


def product(request, pk):
    title = 'product'

    links_menu = ProductCategory.objects.all()
    current_product = get_object_or_404(Product, pk=pk)

    products = Product.objects.filter(
        category__name=current_product.category).exclude(
            pk=current_product.pk).order_by(
                'price')

    context = {
        'title': title,
        'links_menu': links_menu,
        'current_product': current_product,
        'basket': get_basket(request),
        'products': products,
    }

    return render(request=request, template_name='mainapp/product.html', context=context)
