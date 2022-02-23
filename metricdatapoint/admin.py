from django.contrib import admin


from .models import Metricdata, MetricsDataPoint, SpesData
# Register your models here.


admin.site.register(MetricsDataPoint)
admin.site.register(SpesData)
admin.site.register(Metricdata)
