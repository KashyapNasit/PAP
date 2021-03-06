# Generated by Django 2.1.7 on 2019-03-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190329_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pending_join_requests',
            field=models.ManyToManyField(blank=True, related_name='_profile_pending_join_requests_+', to='login.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='preference_of_professor',
            field=models.ManyToManyField(blank=True, related_name='_profile_preference_of_professor_+', to='login.Profile'),
        ),
    ]
