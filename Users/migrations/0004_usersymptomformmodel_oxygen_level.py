# Generated by Django 2.2 on 2021-07-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20210714_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersymptomformmodel',
            name='oxygen_level',
            field=models.IntegerField(default=93, max_length=3),
        ),
    ]
