

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
