# Generated by Django 3.2.8 on 2021-10-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211028_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]