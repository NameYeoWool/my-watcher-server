# Generated by Django 2.2 on 2019-04-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Watcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='notice',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='rooms',
            name='spec',
            field=models.TextField(blank=True),
        ),
    ]
