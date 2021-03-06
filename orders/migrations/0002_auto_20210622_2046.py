# Generated by Django 3.2.4 on 2021-06-22 20:46

from django.db import migrations, models
import django_fsm
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='state',
            field=django_fsm.FSMField(choices=[['Unprocessed', 'Unprocessed'], ['Processing', 'Processing'], ['Processed', 'Processed']], default=orders.models.OrderStates['Unprocessed'], max_length=50, protected=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='Price'),
        ),
    ]
