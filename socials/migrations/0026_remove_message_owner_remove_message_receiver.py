# Generated by Django 4.2.3 on 2023-08-29 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0025_auto_20230527_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
    ]
