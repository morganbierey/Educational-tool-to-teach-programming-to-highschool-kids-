# Generated by Django 2.1.5 on 2023-02-10 02:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_tool', '0007_auto_20230207_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='published',
            field=models.DateField(verbose_name=datetime.date(2023, 2, 10)),
        ),
        migrations.AlterField(
            model_name='project',
            name='upload_file',
            field=models.FileField(max_length=254, upload_to='profile_images'),
        ),
    ]
