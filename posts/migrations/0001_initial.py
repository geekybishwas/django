# Generated by Django 5.0.6 on 2024-06-18 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
