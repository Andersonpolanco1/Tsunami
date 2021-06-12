from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Product'
        ordering = ['name']


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    lastName = models.CharField(max_length=150, verbose_name='Last name')
    DNI = models.CharField(max_length=15, unique=True, verbose_name='DNI')
    birthday = models.DateField(default=datetime.now, verbose_name='Birthday')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Address')
    gender = models.CharField(max_length=1, blank=True, null=True, verbose_name='Gender')

    def __str__(self):
        return "{} {}".format(self.name, self.lastName)

    class Meta:
        db_table = 'Client'
        ordering = ['name']


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dateJoined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.client.name

    class Meta:
        db_table = 'Sale'
        ordering = ['id']


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.0, max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.0, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = 'SaleDetail'
        ordering = ['id']