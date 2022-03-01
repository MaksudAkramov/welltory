from rest_framework import viewsets
from metricdatapoint.models import MetricData
from metricdatapoint.serializers import DataSerializer
from rest_framework.permissions import IsAuthenticated



class DataViewSet(viewsets.ModelViewSet):
    queryset = MetricData.objects.all()
    serializer_class = DataSerializer

    permission_classes = [IsAuthenticated, ]


    def perform_create(self, serializer):
        serializer.save()

