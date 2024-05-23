# Generated by Django 4.2 on 2024-05-23 14:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.CharField(max_length=100)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_digtial', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('stock_status', models.CharField(choices=[('In stock', 'In stock'), ('Investimento', 'Investimento'), ('Backordered', 'Backordered')], default='Investimento', max_length=13)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sku', models.UUIDField(default=uuid.uuid4)),
                ('stock_qty', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('order', models.IntegerField()),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SeasonalEvents',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_qty', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('stock_product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.producttype')),
            ],
        ),
        migrations.CreateModel(
            name='ProductLine_AttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.attributevalue')),
                ('product_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.productline')),
            ],
        ),
        migrations.AddField(
            model_name='productline',
            name='attribute_values',
            field=models.ManyToManyField(related_name='attibute', through='inventory.ProductLine_AttributeValue', to='inventory.attributevalue'),
        ),
        migrations.AddField(
            model_name='productline',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.product'),
        ),
        migrations.CreateModel(
            name='productImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alternative_text', models.CharField(max_length=100)),
                ('url', models.ImageField(upload_to='')),
                ('order', models.IntegerField()),
                ('product_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.productline')),
            ],
        ),
        migrations.CreateModel(
            name='Product_ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.producttype')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ManyToManyField(related_name='product_type', through='inventory.Product_ProductType', to='inventory.producttype'),
        ),
        migrations.AddField(
            model_name='product',
            name='seasonal_events',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.seasonalevents'),
        ),
    ]
