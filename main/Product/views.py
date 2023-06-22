from django.shortcuts import render
from main.Product.models import Products


def contacts(request):
    product_list = Products.objects.all()
    context = {
        'product': product_list
    }
    return render(request, "main/base.html", context)

# def contacts(request):
#     if request.method == "POST":
#         firstname = request.POST.get("firstName")
#         lastname = request.POST.get("lastName")
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         print(f"{firstname}, {lastname}:{username},{email}")
#     return render(request, "main/base.html")