from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from main.Product.forms import ProductForm, SubjectForm
from main.Product.models import Products, Subject

from django.shortcuts import render, redirect

from main.users.models import UserVerification


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Products
    form_class = ProductForm
    success_url = reverse_lazy("Product:create")  # ПЕРЕХОД НА НУЖНУЮ СТРАНИЦУ
    permission_required = "main.Product.add_product"

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin,  UpdateView):
    model = Products
    fields = ("name", "image", "category")
    permission_required = "main.Product.change_product"
    #success_url = reverse_lazy('Blog:list')

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.owner != self.request.user:
    #     raise Http404
    #     return self.object
    #
    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)   # СОХРАНЕНИЕ

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("Product:update", args=[self.kwargs.get('pk')])  # ПРИВЯЗКА ПО ПК

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Products, Subject, form=SubjectForm, extra=1)
        if self.request.method == "POST":  # пост и гет запрос
            context_data["formset"] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()["formset"]
        self.object = form.save()
        if formset.is_valid():  # проверка на валидность возвращение и сохранение
            formset.instance = self.object
            formset.save()

            return super().form_valid(form)

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Products
    template_name = "Product/products_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()    # количество просмотров
        return self.object


class ProductDeleteView(UserPassesTestMixin, DeleteView, LoginRequiredMixin):
    model = Products
    success_url = reverse_lazy("Product:list")

    def test_func(self):
        return self.request.user.is_superuser


# @permission_required('main.Product.change_product')
# @login_required  # уровень доступа к стр
def product(request):
    product_list = Products.objects.all()
    for product in product_list:
        active_version = product.version_set.filter(is_current=True).first()
        product.active_version = active_version  # вывод активной версии
    context = {
        'product': product_list,
        "title": "Главная",
    }
    return render(request, "Product/products_list.html", context)

class ProductListView(LoginRequiredMixin, ListView):
    model = Products
    template_name = "Product/products_list.html"
    permission_required = "Product.view_product"

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

# @login_required  # уровень доступа к стр
def catalog(request, pk):
    context = {
        'product': Products.objects.filter(id=pk),
        "title": "Главная",
    }
    return render(request, "Product/products_detail.html", context)


# @login_required  # уровень доступа к стр
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