# Generated by Django 2.1.7 on 2019-04-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0010_auto_20190413_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='is_mentor_allotted',
            field=models.BooleanField(default=False),
        ),
    ]