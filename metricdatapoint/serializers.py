from rest_framework import serializers,status
from rest_framework.response import Response
from metricdatapoint import models


class SpesDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SpesData
        fields = ['date', 'value']     


class MidSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.MetricsDataPoint
        fields = ['data_type', 'data']


class MetricsDataPointSerializer(serializers.ModelSerializer):
    x = MidSerializer(many=True)
    y = MidSerializer(many=True)

    class Meta:
        model = models.MetricsDataPoint
        fields = ['data_type', 'y']
        

class DataSerializer(serializers.ModelSerializer):
    data = MetricsDataPointSerializer()

    class Meta:
        model = models.Metricdata
        fields = ['user_id', 'data']



    # def create(self, validated_data):
    #     obj = models.MetricsDataPoint.objects.filter(
    #         x_data_type=validated_data['data']['x_data_type'],
    #         y_data_type=validated_data['data']['y_data_type']
    #     ).first()
    #     for item in validated_data['data']['x']:
    #         models.SpesData.objects.create(
    #             date=item['date'],
    #             value=float(item['value']),
    #         )
    #     for item in validated_data['data']['y']:
    #         y_date = item['date']
    #         y_value = item['value']

    #         models.SpesData.objects.create(
    #             date=item['date'],
    #             value=float(item['value']),
    #         )
    #     obj = models.MetricsDataPoint.objects.update_or_create(
    #         x_data_type=validated_data['data']['x_data_type'],
    #         y_data_type=validated_data['data']['y_data_type'],


    #     )    
    #     return Response(obj, status=status.HTTP_200_OK)    