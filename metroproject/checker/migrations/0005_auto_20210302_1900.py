# Generated by Django 3.1.5 on 2021-03-02 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0004_auto_20210227_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friday',
            name='card',
        ),
        migrations.RemoveField(
            model_name='mondaythursday',
            name='card',
        ),
        migrations.RemoveField(
            model_name='saturday',
            name='card',
        ),
        migrations.RemoveField(
            model_name='sunday',
            name='card',
        ),
    ]