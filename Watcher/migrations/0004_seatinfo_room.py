# Generated by Django 2.2 on 2019-04-16 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Watcher', '0003_auto_20190416_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='seatinfo',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Watcher.Room'),
        ),
    ]
