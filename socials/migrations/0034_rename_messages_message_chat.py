# Generated by Django 4.2.3 on 2023-08-29 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0033_remove_chat_messages_message_messages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='messages',
            new_name='chat',
        ),
    ]