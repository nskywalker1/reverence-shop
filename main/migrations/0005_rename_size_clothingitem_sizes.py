# Generated by Django 5.2 on 2025-04-05 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_clothingitem_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothingitem',
            old_name='size',
            new_name='sizes',
        ),
    ]
