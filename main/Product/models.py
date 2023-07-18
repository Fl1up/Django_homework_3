from django.db import models
# Create your models here.
from django.db import models
from django.urls import reverse

from main import users

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
    name = models.CharField(max_length=100, verbose_name="Название", unique=True) # unique - уникальность
    description = models.TextField(max_length=100, verbose_name="Описание", **NULLABLE)
    image = models.ImageField(upload_to='media/', verbose_name="Фото", **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    purchase_price = models.IntegerField(default=0, verbose_name="Цена за покупку")
    date_of_creation = models.DateField(default='2023-06-20', verbose_name="Дата создания")
    last_modified_date = models.DateField(default='2023-06-20', verbose_name="Дата последнего изменения")
    is_published = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return f"{self.name} {self.description} {self.image} {self.category} " \
               f"{self.purchase_price} {self.date_of_creation} {self.last_modified_date}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Version(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    version_number = models.CharField(max_length=50)
    version_name = models.CharField(max_length=100)  # версия продукта
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.version_name


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="описание")

    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="продукты")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "предмет"
        verbose_name_plural = "предметы"

