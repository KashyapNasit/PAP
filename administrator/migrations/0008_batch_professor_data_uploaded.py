# Generated by Django 2.1.7 on 2019-04-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0007_auto_20190409_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='professor_data_uploaded',
            field=models.BooleanField(default=False),
        ),
    ]
