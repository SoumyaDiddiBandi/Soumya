# Generated by Django 3.0.2 on 2020-02-05 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_pic',
            name='image',
            field=models.FilePathField(path='home/img'),
        ),
    ]