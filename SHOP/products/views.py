from django.shortcuts import render
from products.models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    assert isinstance(request, object)
    return render(request, 'products/product.html', locals())