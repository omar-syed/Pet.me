# Generated by Django 4.2.7 on 2023-11-18 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_alter_message_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created_at']},
        ),
    ]
