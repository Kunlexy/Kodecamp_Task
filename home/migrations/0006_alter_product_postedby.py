# Generated by Django 4.0.4 on 2022-06-08 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_bio_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='postedby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.people'),
        ),
    ]