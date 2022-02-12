from django.db import models
from datetime import date

# Create your models here.
CHOICES =[     
    ("AVG_HEARTBEAT", 'avg_heartbeat'),
    ("CALORIES_CONSUMED", 'calories_consumed'),
    ("SLEEP_HOURS", 'sleep_hours'),
    ("MORNING_PULSE", 'morning_pulse')]


class MetricDataPoint(models.Model):
    x_data_type=models.CharField(max_length=100,choices= CHOICES)
    y_data_type=models.CharField(max_length=100,choices= CHOICES)
    x_date = models.DateField(default=date.today())
    y_date = models.DateField(default=date.today())
    x_values = models.FloatField()
    y_values = models.FloatField()