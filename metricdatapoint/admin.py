from django.contrib import admin


from .models import MetricData, MetricsDataPoint, SpesData
# Register your models here.


admin.site.register(MetricData)
admin.site.register(MetricsDataPoint)
admin.site.register(SpesData)

