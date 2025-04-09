# Generated by Django 5.2 on 2025-04-09 11:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0008_itemimage'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('house_number', models.CharField(max_length=10)),
                ('apartment_number', models.CharField(max_length=10)),
                ('postal_code', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tracking_number', models.CharField(blank=True, default='Pending', max_length=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('canceled', 'Canceled')], default='pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('clothing_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.clothingitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.size')),
            ],
            options={
                'verbose_name': 'Order item',
                'verbose_name_plural': 'Order items',
            },
        ),
    ]
