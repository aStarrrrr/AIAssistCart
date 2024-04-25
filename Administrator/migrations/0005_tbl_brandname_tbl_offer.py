# Generated by Django 5.0.2 on 2024-03-08 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0004_rename_admin_category_tbl_category_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_brandname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_name', models.CharField(max_length=50)),
                ('offer_fromdate', models.CharField(max_length=50)),
                ('offer_todate', models.CharField(max_length=50)),
                ('offer_discription', models.CharField(max_length=50)),
            ],
        ),
    ]
