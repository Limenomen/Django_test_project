# Generated by Django 3.2.5 on 2021-09-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/movies/', verbose_name='Изображение'),
        ),
    ]
