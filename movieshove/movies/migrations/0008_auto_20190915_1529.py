# Generated by Django 2.2.4 on 2019-09-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20190915_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='images/default.jpg', upload_to='media/images/'),
        ),
    ]
