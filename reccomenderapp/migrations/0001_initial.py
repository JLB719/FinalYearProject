# Generated by Django 3.2.9 on 2022-03-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('maxyear', models.IntegerField()),
                ('numberofepisodes', models.IntegerField()),
                ('languages', models.TextField()),
                ('origincountries', models.TextField()),
                ('likedgenres', models.TextField()),
                ('dislikedgenres', models.TextField()),
                ('likedshows', models.TextField()),
                ('dislikedshows', models.TextField()),
            ],
        ),
    ]
