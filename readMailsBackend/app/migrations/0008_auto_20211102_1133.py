# Generated by Django 3.2.8 on 2021-11-02 11:33

import app.models
from django.db import migrations, models
import enumchoicefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211102_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='last_changed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=enumchoicefield.fields.EnumChoiceField(default=app.models.PRIORITY(1), enum_class=app.models.PRIORITY, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='time_created',
            field=models.DateTimeField(null=True),
        ),
    ]
