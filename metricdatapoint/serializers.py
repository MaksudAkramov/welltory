from rest_framework import serializers
from metricdatapoint import models
class AccountSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        
        data = models.MetricDataPoint.objects.create(**validated_data)
        return data 

    class Meta:
        
        model = models.MetricDataPoint
        fields = ['x_data_type', 'x_date', 'x_values', 'y_data_type', 'y_date', 'y_values']