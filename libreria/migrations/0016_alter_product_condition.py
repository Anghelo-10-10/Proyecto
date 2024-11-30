# Generated by Django 4.2 on 2024-08-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0015_alter_product_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('Mal estado', 'Mal estado'), ('Usado', 'Usado'), ('Nuevo', 'Nuevo')], max_length=30),
        ),
    ]