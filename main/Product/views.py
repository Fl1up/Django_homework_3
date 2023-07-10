from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from main.Product.models import Products


class ProductCreateView(CreateView):
    model = Products
    fields = ("name", "category")
    success_url = reverse_lazy("Product:create")

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Products
    fields = ('name', "description")
    #success_url = reverse_lazy('Blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("Product:update", args=[self.kwargs.get('pk')])


class ProductListView(ListView):
    model = Products

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ProductDetailView(DetailView):
    model = Products

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()    # количество просмотров
        return self.object


class ProductDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy("Product:list")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        massage = request.POST.get("massage")
        print(f"{name}\n{email}\n{massage}")
    context = {
        "title": "Контакты",
    }
    return render(request, "Product/contact.html", context)






def product(request):
    product_list = Products.objects.all()
    context = {
        'product': product_list,
        "title": "Главная",
    }
    return render(request, "Product/products_list.html", context)
def catalog(request,pk):
    context = {
        'product': Products.objects.filter(id=pk),
        "title": "Главная",
    }
    return render(request, "Product/products_detail.html", context)







