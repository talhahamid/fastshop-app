# Generated by Django 4.1.7 on 2024-02-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fastshop', '0003_remove_orders_user_orders_customername'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='city',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]