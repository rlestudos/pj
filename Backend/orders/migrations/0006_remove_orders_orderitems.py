# Generated by Django 2.2.2 on 2019-06-24 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_orders_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='orderItems',
        ),
    ]
