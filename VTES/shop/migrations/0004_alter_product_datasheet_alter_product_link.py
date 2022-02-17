# Generated by Django 4.0.2 on 2022-02-17 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_shop_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datasheet',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to='datasheet', verbose_name='فایل و Datasheet'),
        ),
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='لینک محصول'),
        ),
    ]