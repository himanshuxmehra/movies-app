# Generated by Django 2.2.4 on 2019-10-16 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20191016_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
    ]
