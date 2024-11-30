# Generated by Django 4.2 on 2024-08-16 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_alter_product_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('Mal estado', 'Mal estado'), ('Nuevo', 'Nuevo'), ('Usado', 'Usado')], max_length=30),
        ),
    ]
