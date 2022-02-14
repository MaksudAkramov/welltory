from django.db import models
from datetime import date

from user.models import Account


CHOICES =[     
    ("AVG_HEARTBEAT", 'avg_heartbeat'),
    ("CALORIES_CONSUMED", 'calories_consumed'),
    ("SLEEP_HOURS", 'sleep_hours'),
    ("MORNING_PULSE", 'morning_pulse')]


class SpesData(models.Model):
    date = models.DateField()
    value = models.FloatField()



class MetricsDataPoint(models.Model):
    x_data_type=models.CharField(max_length=100, choices=CHOICES)
    y_data_type=models.CharField(max_length=100, choices=CHOICES)
    x = models.ForeignKey(SpesData, on_delete=models.CASCADE, null=True, related_name='x_data')
    y = models.ForeignKey(SpesData, on_delete=models.CASCADE, null=True, related_name='y_data')



class MetricData(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    data = models.ForeignKey(MetricsDataPoint, on_delete=models.CASCADE, null=True)


