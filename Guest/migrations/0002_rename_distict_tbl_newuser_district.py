# Generated by Django 5.0.2 on 2024-03-09 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_newuser',
            old_name='distict',
            new_name='district',
        ),
    ]