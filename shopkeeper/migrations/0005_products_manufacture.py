# Generated by Django 4.1.7 on 2024-01-31 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopkeeper', '0004_products_forwhom_products_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='manufacture',
            field=models.DateField(default='2000-2-1'),
            preserve_default=False,
        ),
    ]