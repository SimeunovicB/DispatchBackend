# Generated by Django 3.2.8 on 2021-11-08 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_lead_notes_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='time',
            field=models.CharField(max_length=255, null=True),
        ),
    ]