# Generated by Django 3.2 on 2023-05-26 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0021_alter_product_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='post',
        ),
    ]
