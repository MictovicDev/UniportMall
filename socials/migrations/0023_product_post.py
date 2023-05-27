# Generated by Django 3.2 on 2023-05-26 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0022_remove_product_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='socials.post'),
        ),
    ]