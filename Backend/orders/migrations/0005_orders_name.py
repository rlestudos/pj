# Generated by Django 2.2.2 on 2019-06-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190623_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
