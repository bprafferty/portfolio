# Generated by Django 3.0.2 on 2020-02-20 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bio',
            name='email',
        ),
        migrations.RemoveField(
            model_name='bio',
            name='phone',
        ),
    ]