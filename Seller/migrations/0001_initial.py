# Generated by Django 5.0.2 on 2024-03-17 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administrator', '0010_tbl_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.CharField(max_length=50)),
                ('product_details', models.CharField(max_length=50)),
                ('product_photo', models.FileField(upload_to='Assets/ProductPhoto/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_brandname')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.tbl_subcategory')),
            ],
        ),
    ]
