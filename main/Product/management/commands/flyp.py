from django.core.management.base import BaseCommand
from main.Product.models import Products, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Products.objects.all().delete()
        Category.objects.all().delete()

        fruits = Category.objects.create(name='фрукты')
        vegetables = Category.objects.create(name='овощи')
        berry = Category.objects.create(name='ягоды')
        meet = Category.objects.create(name='мясо')

        Products.objects.create(name='банан', description='', purchase_price='146', category=fruits)
        Products.objects.create(name='помидор', description='', purchase_price='120', category=vegetables)
        Products.objects.create(name='орех', description='', purchase_price='250', category=berry)
        Products.objects.create(name='баранина', description='', purchase_price='600', category=meet)
        Products.objects.create(name='курица', description='', purchase_price='350', category=meet)






