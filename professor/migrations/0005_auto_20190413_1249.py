# Generated by Django 2.1.7 on 2019-04-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0004_auto_20190413_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
