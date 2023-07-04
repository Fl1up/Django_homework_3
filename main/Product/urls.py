from django.urls import path
from main.Product.apps import ProductConfig
from main.Product.views import product, contact, catalog, ProductListView , DetailView

app_name = ProductConfig.name

urlpatterns = [
    path("", product, name='product'),
    path("contact/", contact, name='contact'),
    path("catalog/<int:pk>", catalog, name='catalog'),
]

