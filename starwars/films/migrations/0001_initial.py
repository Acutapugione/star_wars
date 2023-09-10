# Generated by Django 4.2.5 on 2023-09-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('episode_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=120)),
                ('opening_crawl', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
