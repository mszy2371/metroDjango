# Generated by Django 3.1.5 on 2021-03-07 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0005_auto_20210302_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoorCodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=40)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
    ]
