# Generated by Django 4.0.7 on 2022-09-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='latitude',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='longitude',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
