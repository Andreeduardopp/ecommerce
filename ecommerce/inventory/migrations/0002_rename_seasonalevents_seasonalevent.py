# Generated by Django 5.0.1 on 2024-01-31 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SeasonalEvents',
            new_name='SeasonalEvent',
        ),
    ]