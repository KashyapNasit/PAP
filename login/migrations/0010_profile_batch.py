# Generated by Django 2.1.7 on 2019-04-10 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0008_batch_professor_data_uploaded'),
        ('login', '0009_remove_profile_pending_join_requests'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='batch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.Batch'),
        ),
    ]
