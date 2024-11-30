# Generated by Django 4.2 on 2024-08-16 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0008_alter_product_condition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase_detail',
            old_name='unit_price_product',
            new_name='subtotal',
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('Mal estado', 'Mal estado'), ('Nuevo', 'Nuevo'), ('Usado', 'Usado')], max_length=30),
        ),
        migrations.AlterField(
            model_name='purchase_detail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='libreria.product'),
        ),
    ]