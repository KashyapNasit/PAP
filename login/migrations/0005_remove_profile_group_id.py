# Generated by Django 2.1.7 on 2019-03-30 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_remove_profile_preference_of_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='group_id',
        ),
    ]
