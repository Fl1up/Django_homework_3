from django.views.generic import ListView, DetailView

from django.shortcuts import render
from main.Product.models import Products

#_____________________________________
class ProductListView(ListView):
    model = Products
    template_name = "main/product.html"

class CatalogDetailView(DetailView):
    model = Products
    template_name = "main/catalog.html"
#_____________________________________
def product(request):
    product_list = Products.objects.all()
    context = {
        'product': product_list,
        "title": "Главная",
    }
    return render(request, "main/product.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("massage")
        print(f"{name}\n{email}\n{massage}")
    context = {
        "title": "Контакты",
    }
    return render(request, "main/contact.html", context)


def catalog(request,pk):
    product_list = Products.objects.get(pk=pk)
    context = {
        'product': Products.objects.filter(id=pk),
        "title": "Главная",
    }
    return render(request, "main/catalog.html", context)

