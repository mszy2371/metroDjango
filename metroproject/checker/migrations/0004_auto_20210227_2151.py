# Generated by Django 3.1.5 on 2021-02-27 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0003_auto_20210206_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friday',
            name='card',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='mondaythursday',
            name='card',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='saturday',
            name='card',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='sunday',
            name='card',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
