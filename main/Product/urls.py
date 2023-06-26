
from django.urls import path

from . import views

from main.Product.apps import ProductConfig
from main.Product.views import product, contact, catalog

app_name = ProductConfig.name

urlpatterns = [
    path("", product, name='product'),
    path("contact/", contact, name='contact'),
    path("catalog/", catalog, name='catalog'),
]

