# Generated by Django 5.1.2 on 2025-01-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='bg.jpg', max_length=50, null=0),
        ),
    ]
