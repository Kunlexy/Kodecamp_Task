# Generated by Django 4.0.4 on 2022-06-08 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_product_postedby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='postedby',
        ),
    ]
