from django.urls import path
from main.Product.apps import ProductConfig
from main.Product.views import product, contact, catalog, ProductListView, ProductUpdateView, ProductCreateView, \
    ProductDetailView, ProductDeleteView

app_name = ProductConfig.name

urlpatterns = [
    path('', product, name='list'), #ProductListView
    path("contact/", contact, name='contact'),
    path("catalog/<int:pk>", catalog, name='catalog'), #ProductDetailView
    path("create/", ProductCreateView.as_view(), name="create"),
    path("edit/<int:pk>/", ProductUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="delete"),
]

