# Generated by Django 3.0.2 on 2020-11-02 21:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_project_hidden_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='hidden_date',
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
