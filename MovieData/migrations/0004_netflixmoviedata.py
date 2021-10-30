# Generated by Django 3.2.7 on 2021-10-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MovieData', '0003_delete_netflixmoviedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetflixMovieData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('premiere', models.CharField(max_length=50)),
                ('runtime', models.CharField(max_length=30)),
                ('imdb_score', models.CharField(max_length=30)),
                ('lanaguage', models.CharField(max_length=100)),
            ],
        ),
    ]
