# Generated by Django 3.2.12 on 2022-03-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0015_category_catsub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catsub',
            field=models.BooleanField(default=False),
        ),
    ]
