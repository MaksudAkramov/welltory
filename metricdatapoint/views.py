from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from metricdatapoint.models import MetricData
from metricdatapoint.serializers import DataSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = MetricData.objects.all()
    serializer_class = DataSerializer


    # @action(methods=['post'], detail=False, url_path='me')
    # def get_me(self, request):
    #     serializer = self.get_serializer(request.user)
    #     return Response(serializer.data)