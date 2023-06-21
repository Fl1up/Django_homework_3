from django.db import models
# Create your models here.
from django.db import models

NULLABLE = {"blank": True, "null": True}
ABLE = {"blank": False, "null": False}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=100, verbose_name="Описание", **NULLABLE)

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=100, verbose_name="Описание", **NULLABLE)
    imag = models.ImageField(upload_to="products/", verbose_name="Фото", **NULLABLE)
    #category = models.CharField(max_length=100, verbose_name="Категория")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    purchase_price = models.IntegerField(default=0, verbose_name="Цена за покупку")
    date_of_creation = models.DateField(default='2023-06-20', verbose_name="Дата создания")
    last_modified_date = models.DateField(default='2023-06-20', verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.name} {self.description} {self.imag} {self.category} " \
               f"{self.purchase_price} {self.date_of_creation} {self.last_modified_date}"

    class Mata:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"