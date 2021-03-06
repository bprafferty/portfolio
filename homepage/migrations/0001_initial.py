# Generated by Django 3.0.2 on 2020-02-20 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.FilePathField(path='/media/pictures/profile')),
                ('objective', models.TextField()),
                ('education', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
            ],
        ),
    ]
