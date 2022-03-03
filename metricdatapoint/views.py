from rest_framework import viewsets
from metricdatapoint.models import MetricDataPoint
from metricdatapoint.serializers import DataSerializer, GetDataSerializer
from rest_framework.permissions import IsAuthenticated


class DataViewSet(viewsets.ModelViewSet):
    queryset = MetricDataPoint.objects.all()
    serializer_action_classes = {
        'get': GetDataSerializer,
        'post': DataSerializer
    }

    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action == "get":
            return GetDataSerializer
        return DataSerializer

    def perform_create(self, serializer):
        serializer.save()
