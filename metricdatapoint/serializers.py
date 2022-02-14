from rest_framework import serializers
from metricdatapoint import models

class SpesDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SpesData
        fields = ['date', 'value']     



class MetricsDataPointSerializer(serializers.ModelSerializer):
    x = SpesDataSerializer()
    y = SpesDataSerializer()



    class Meta:
        model = models.MetricsDataPoint
        fields = ['x_data_type', 'y_data_type', 'x', 'y']     

class DataSerializer(serializers.ModelSerializer):
    data = MetricsDataPointSerializer()

    class Meta:
        
        model = models.MetricData
        fields = ['user_id', 'data']

