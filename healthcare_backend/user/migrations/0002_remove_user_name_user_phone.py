# Generated by Django 5.2.4 on 2025-07-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='0000000000', max_length=10, unique=True),
        ),
    ]
