# Generated by Django 3.0.2 on 2020-02-21 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20200220_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='media/pictures/profile/default_project.jpg', upload_to='pictures/project'),
        ),
    ]
