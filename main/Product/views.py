from django.shortcuts import render


def contacts(request):
    if request.method == "POST":
        firstname = request.POST.get("firstName")
        lastname = request.POST.get("lastName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        print(f"{firstname}, {lastname}:{username},{email}")
    return render(request, "main/index.html")