# Generated by Django 3.2.4 on 2021-06-18 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_order_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='name',
        ),
    ]
