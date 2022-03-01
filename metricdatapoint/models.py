from django.db import models

from user.models import Account



CHOICES =[     
    ("avg_heartbeat", 'AVG_HEARTBEAT'),
    ("calories_consumed", 'CALORIES_CONSUMED'),
    ("sleep_hours", 'SLEEP_HOURS'),
    ("morning_pulse", 'MORNING_PULSE')
]


class SpesData(models.Model):
    date = models.DateField()
    value = models.FloatField()



class MetricDataPoint(models.Model):
    x_data_type = models.CharField(max_length=100, choices=CHOICES, null=True)
    y_data_type = models.CharField(max_length=100, choices=CHOICES, null=True)
    x = models.ForeignKey(SpesData, on_delete=models.CASCADE, null=True, related_name='x_data')
    y = models.ForeignKey(SpesData, on_delete=models.CASCADE, null=True, related_name='y_data')



class MetricData(models.Model):
    user_id = models.IntegerField()
    data = models.ForeignKey(MetricDataPoint, on_delete=models.CASCADE, null=True)


