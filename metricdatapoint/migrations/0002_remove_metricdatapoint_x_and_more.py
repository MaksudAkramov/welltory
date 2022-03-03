# Generated by Django 4.0.2 on 2022-03-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metricdatapoint', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metricdatapoint',
            name='x',
        ),
        migrations.RemoveField(
            model_name='metricdatapoint',
            name='x_data_type',
        ),
        migrations.RemoveField(
            model_name='metricdatapoint',
            name='y',
        ),
        migrations.RemoveField(
            model_name='metricdatapoint',
            name='y_data_type',
        ),
        migrations.AddField(
            model_name='metricdatapoint',
            name='data_type',
            field=models.CharField(choices=[('avg_heartbeat', 'AVG_HEARTBEAT'), ('calories_consumed', 'CALORIES_CONSUMED'), ('sleep_hours', 'SLEEP_HOURS'), ('morning_pulse', 'MORNING_PULSE')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='metricdatapoint',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='metricdatapoint',
            name='value',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='SpesData',
        ),
    ]