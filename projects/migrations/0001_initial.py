# Generated by Django 4.0.1 on 2022-01-19 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technologies', models.CharField(max_length=100)),
                ('image', models.FilePathField(path='/img')),
                ('link', models.URLField()),
            ],
        ),
    ]
