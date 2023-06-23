
from django.shortcuts import render
from main.Product.models import Products


def product(request):
    product_list = Products.objects.all()
    context = {
        'product': product_list,
        "title": "Главная",
    }
    return render(request, "main/product.html", context)


def contact(request):
    context = {
        "title": "Контакты",
    }
    return render(request, "main/contact.html", context)


def catalog(request):
    product_list = Products.objects.all()
    context = {
        'product': product_list,
        "title": "Главная",
    }
    return render(request, "main/catalog.html", context)

