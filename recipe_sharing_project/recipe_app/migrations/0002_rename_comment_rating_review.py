# Generated by Django 5.1.3 on 2024-11-14 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='comment',
            new_name='review',
        ),
    ]
