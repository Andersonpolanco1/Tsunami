# Generated by Django 3.0.4 on 2021-06-11 22:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Name')),
            ],
            options={
                'db_table': 'Category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('lastName', models.CharField(max_length=150, verbose_name='Last name')),
                ('DNI', models.CharField(max_length=15, unique=True, verbose_name='DNI')),
                ('birthday', models.DateField(default=datetime.datetime.now, verbose_name='Birthday')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Address')),
                ('gender', models.CharField(blank=True, max_length=1, null=True, verbose_name='Gender')),
            ],
            options={
                'db_table': 'Client',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d')),
                ('pvp', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Category')),
            ],
            options={
                'db_table': 'Product',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateJoined', models.DateField(default=datetime.datetime.now)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Client')),
            ],
            options={
                'db_table': 'Sale',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('quantity', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprise.Sale')),
            ],
            options={
                'db_table': 'SaleDetail',
                'ordering': ['id'],
            },
        ),
    ]
