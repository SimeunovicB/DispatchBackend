# Generated by Django 3.2.8 on 2021-11-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_rename_senderr_note_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='notes_active',
            field=models.BooleanField(default=False),
        ),
    ]
