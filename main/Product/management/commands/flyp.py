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
        fish = Category.objects.create(name='рыба')

        Products.objects.create(name='банан', description='', purchase_price='146', category=fruits, image="/Банан.png")
        Products.objects.create(name='помидор', description='', purchase_price='120', category=vegetables, image='/Помидор.png')
        Products.objects.create(name='орех', description='', purchase_price='250', category=berry, image='/Орех.png')
        Products.objects.create(name='баранина', description='', purchase_price='600', category=meet, image='/Баранина.png')
        Products.objects.create(name='курица', description='', purchase_price='350', category=meet, image='/Курица.png')
        Products.objects.create(name='килька', description='', purchase_price='700', category=fish, image='/Рыба.png')






