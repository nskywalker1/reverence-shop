# Generated by Django 5.2 on 2025-04-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_size_clothingitem_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothingitem',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]
