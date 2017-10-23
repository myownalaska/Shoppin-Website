from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def ishop(request):
    name = "alya"
    current_day = "27.09.2017"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'pages/index.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    return render(request, 'pages/home.html', locals())

