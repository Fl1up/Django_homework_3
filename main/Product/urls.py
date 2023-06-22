from django.urls import path

from main.Product.views import contacts

app_name = 'contact'

urlpatterns = [
     path("", contacts)
 ]

