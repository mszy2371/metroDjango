# Generated by Django 3.1.5 on 2021-02-06 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0002_auto_20210204_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rota',
            name='friday',
            field=models.ForeignKey(db_column='Friday', on_delete=django.db.models.deletion.CASCADE, related_name='fri_rota', to='checker.friday', verbose_name='Friday'),
        ),
        migrations.AlterField(
            model_name='rota',
            name='monday',
            field=models.ForeignKey(db_column='Monday', on_delete=django.db.models.deletion.CASCADE, related_name='mon_rota', to='checker.mondaythursday', verbose_name='Monday'),
        ),
        migrations.AlterField(
            model_name='rota',
            name='saturday',
            field=models.ForeignKey(db_column='Saturday', on_delete=django.db.models.deletion.CASCADE, related_name='sat_rota', to='checker.saturday', verbose_name='Saturday'),
        ),
        migrations.AlterField(
            model_name='rota',
            name='sunday',
            field=models.ForeignKey(db_column='Sunday', on_delete=django.db.models.deletion.CASCADE, related_name='sun_rota', to='checker.sunday', verbose_name='Sunday'),
        ),
        migrations.AlterField(
            model_name='rota',
            name='thursday',
            field=models.ForeignKey(db_column='Thursday', on_delete=django.db.models.deletion.CASCADE, related_name='thu_rota', to='checker.mondaythursday', verbose_name='Thursday'),
        ),
        migrations.AlterField(
            model_name='rota',
            name='tuesday',
            field=models.ForeignKey(db_column='Tuesday', on_delete=django.db.models.deletion.CASCADE, related_name='tue_rota', to='checker.mondaythursday', verbose_name='Tuesday'),
        ),
        migrations.AlterField(
            model_name='rota',
            name='wednesday',
            field=models.ForeignKey(db_column='Wednesday', on_delete=django.db.models.deletion.CASCADE, related_name='wed_rota', to='checker.mondaythursday', verbose_name='Wednesday'),
        ),
    ]
