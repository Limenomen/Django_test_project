# Generated by Django 3.2.5 on 2021-08-22 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_movie_actors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
    ]
