# Generated by Django 4.0.7 on 2022-09-27 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_photo_mimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='Mimage',
        ),
    ]