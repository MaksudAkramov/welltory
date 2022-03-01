from rest_framework import serializers 
from metricdatapoint import models


class SpesDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SpesData
        fields = ['date', 'value']     



class MetricDataPointSerializer(serializers.ModelSerializer):
    x = SpesDataSerializer()
    y = SpesDataSerializer()

    class Meta:
        model = models.MetricDataPoint
        fields = ['x_data_type', 'y_data_type', 'x', 'y']
        

class DataSerializer(serializers.ModelSerializer):
    data = MetricDataPointSerializer()

    class Meta:
        model = models.MetricData
        fields = ['user_id', 'data']



    def create(self, validated_data):
        x = models.SpesData.objects.create(date=validated_data["data"]["x"]["date"], value=validated_data["data"]["x"]["value"])  
        y = models.SpesData.objects.create(date=validated_data["data"]["y"]["date"], value=validated_data["data"]["y"]["value"])    
        obj = models.MetricDataPoint.objects.update_or_create(
            x_data_type=validated_data['data']['x_data_type'],
            y_data_type=validated_data['data']['y_data_type'],
            x=x,
            y=y)
            
        overall_data = models.MetricData.objects.update_or_create(user_id=validated_data['user_id'], data=obj[0])
        return overall_data