# Generated by Django 2.2 on 2021-07-14 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersymptomformmodel',
            name='address',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='usersymptomformmodel',
            name='cold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usersymptomformmodel',
            name='cough',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usersymptomformmodel',
            name='fever',
            field=models.BooleanField(default=False),
        ),
    ]
