# Generated by Django 2.2.4 on 2019-10-16 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_movie_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
    ]
