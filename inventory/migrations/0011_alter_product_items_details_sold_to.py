# Generated by Django 3.2.3 on 2021-05-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_product_items_details_selling_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_items_details',
            name='sold_to',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
