# Generated by Django 3.2 on 2021-04-29 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orderitem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='+7', max_length=12, verbose_name='Номер телефона'),
        ),
    ]
