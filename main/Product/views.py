
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render
from main.Product.models import Products

#_____________________________________
class ProductListView(ListView):
    model = Products
    template_name = "main/products_list.html"
    context_object_name = "object_list"
    extra_context = {"title": "Главная"}
class ProductDetailView(DetailView):
    model = Products
    template_name = "main/products_detail.html"

class ProductCreateView(CreateView):
    model = Products
    fields = ("name", "category")
    success_url = reverse_lazy("main:create_product")

class ProductUpdateView(UpdateView):
    model = Products
    fields = ("name", "category")
    success_url = reverse_lazy("main:update_product")

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

class ProductDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy("main:product_list")









def product(request):
    product_list = Products.objects.all()
    context = {
        'product': product_list,
        "title": "Главная",
    }
    return render(request, "main/products_list.html", context)

def catalog(request,pk):
    context = {
        'product': Products.objects.filter(id=pk),
        "title": "Главная",
    }
    return render(request, "main/products_detail.html", context)







