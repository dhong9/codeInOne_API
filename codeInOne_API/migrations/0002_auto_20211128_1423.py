# Generated by Django 3.2.9 on 2021-11-28 22:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codeInOne_API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='challengeDesc',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='challenge',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 28, 22, 23, 2, 493756, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='challengeName',
            field=models.CharField(default='', max_length=200),
        ),
    ]
