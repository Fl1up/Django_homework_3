from django.urls import path

from main.Product.views import contacts

urlpatterns = [
     path("", contacts)
 ]

