# Generated by Django 3.2 on 2023-03-31 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0006_auto_20230331_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=82, on_delete=django.db.models.deletion.CASCADE, to='socials.post'),
            preserve_default=False,
        ),
    ]
