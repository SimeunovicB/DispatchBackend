# Generated by Django 3.2.8 on 2021-11-05 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_rename_sender_note_senderr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='senderr',
            new_name='sender',
        ),
    ]
