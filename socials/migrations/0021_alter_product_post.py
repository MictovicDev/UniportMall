# Generated by Django 3.2 on 2023-05-23 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0020_rename_product_product_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='post',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='socials.post'),
        ),
    ]
