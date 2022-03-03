from django.db import models

from user.models import Account








class MetricDataPoint(models.Model):

    CHOICES =[     
        ("avg_heartbeat", 'AVG_HEARTBEAT'),
        ("calories_consumed", 'CALORIES_CONSUMED'),
        ("sleep_hours", 'SLEEP_HOURS'),
        ("morning_pulse", 'MORNING_PULSE')
    ]

    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=50, choices=CHOICES, null=True)
    date = models.DateField(null=True)
    value = models.FloatField(null=True)


    def __str__(self) -> str:
        return self.data_type
    

    




