# Generated by Django 2.0 on 2018-08-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=120)),
                ('album_title', models.CharField(max_length=120)),
                ('genre', models.CharField(max_length=120)),
                ('album_logo', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=120)),
                ('song_title', models.CharField(max_length=120)),
                ('file_type', models.CharField(max_length=120)),
            ],
        ),
    ]
