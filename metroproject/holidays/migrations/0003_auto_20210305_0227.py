# Generated by Django 3.1.5 on 2021-03-05 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0002_auto_20210305_0215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='earlywinter',
            name='id',
        ),
        migrations.AlterField(
            model_name='driver',
            name='block',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='earlywinter',
            name='block',
            field=models.CharField(default=True, max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='latewinter',
            name='block',
            field=models.CharField(max_length=2),
        ),
    ]
