# Generated by Django 3.2.12 on 2022-03-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='featured_image/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
