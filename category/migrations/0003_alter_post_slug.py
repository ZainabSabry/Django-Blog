# Generated by Django 3.2.12 on 2022-03-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=150, unique_for_date='publish_date'),
        ),
    ]
