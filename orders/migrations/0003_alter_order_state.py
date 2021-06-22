# Generated by Django 3.2.4 on 2021-06-22 20:51

from django.db import migrations
import django_fsm
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210622_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=django_fsm.FSMField(choices=[['Unprocessed', 'Unprocessed'], ['Processing', 'Processing'], ['Processed', 'Processed']], default=orders.models.OrderStates['Unprocessed'], max_length=11, protected=True, verbose_name='State'),
        ),
    ]
