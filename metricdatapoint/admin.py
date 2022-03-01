from django.contrib import admin


from .models import MetricDataPoint, MetricData, SpesData



admin.site.register(MetricData)
admin.site.register(SpesData)
admin.site.register(MetricDataPoint)
