# Generated by Django 2.2 on 2021-07-13 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSymptomFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone_no', models.IntegerField()),
                ('address', models.TextField()),
                ('cough', models.BooleanField()),
                ('cold', models.BooleanField()),
                ('fever', models.BooleanField()),
            ],
        ),
    ]
