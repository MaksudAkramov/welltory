from rest_framework import viewsets
from metricdatapoint.models import MetricsDataPoint
from metricdatapoint.serializers import DataSerializer



class DataViewSet(viewsets.ModelViewSet):
    queryset = MetricsDataPoint.objects.all()
    serializer_class = DataSerializer


    def perform_create(self, serializer):
        serializer.save()

