# Generated by Django 3.2.8 on 2021-11-05 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_note_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]