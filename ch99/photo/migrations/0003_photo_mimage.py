# Generated by Django 4.0.7 on 2022-09-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_album_owner_photo_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='Mimage',
            field=models.ImageField(blank=True, null=True, upload_to='Mimages/'),
        ),
    ]
