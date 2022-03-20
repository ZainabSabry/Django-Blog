# Generated by Django 3.2.12 on 2022-03-18 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=150, unique_for_date='publish_date'),
        ),
    ]
