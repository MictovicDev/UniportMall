# Generated by Django 3.2 on 2023-05-23 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0018_alter_like_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='socials.post'),
        ),
    ]