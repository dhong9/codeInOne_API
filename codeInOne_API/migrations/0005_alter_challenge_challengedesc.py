# Generated by Django 3.2.9 on 2021-11-28 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeInOne_API', '0004_remove_challenge_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='challengeDesc',
            field=models.TextField(),
        ),
    ]