# Generated by Django 4.2 on 2024-05-23 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_category_parent_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pid',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seasonal_events',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.seasonalevents'),
        ),
    ]