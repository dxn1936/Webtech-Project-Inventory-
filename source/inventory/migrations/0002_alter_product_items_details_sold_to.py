# Generated by Django 3.2.3 on 2021-05-26 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_items_details',
            name='sold_to',
            field=models.CharField(blank=True, choices=[('Amazon', 'Amazon'), ('Ebay', 'Ebay'), ('Flipkart', 'Flipkart')], max_length=50, null=True),
        ),
    ]
