from django.urls import path
from main.Product.apps import ProductConfig
from main.Product.views import product, contact, catalog, ProductListView, ProductUpdateView, ProductCreateView, \
    ProductDetailView, ProductDeleteView

app_name = ProductConfig.name

urlpatterns = [
    path('', product, name='product_list'), #ProductListView
    path("contact/", contact, name='contact'),
    path("catalog/<int:pk>", catalog, name='detail_product'), #ProductDetailView
    path("create/", ProductCreateView.as_view(), name="create_product"),
    path("edit/<int:pk>/", ProductUpdateView.as_view(), name="update_product"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="delete_product"),
]

