from rest_framework import serializers 
from metricdatapoint import models


class SpesDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MetricDataPoint
        fields = ['date', 'value']     



class MetricDataPointSerializer(serializers.ModelSerializer):
    x_data_type = serializers.ChoiceField(choices=models.MetricDataPoint.CHOICES)
    y_data_type = serializers.ChoiceField(choices=models.MetricDataPoint.CHOICES)
    x = SpesDataSerializer(many=True)
    y = SpesDataSerializer(many=True)

    class Meta:
        model = models.MetricDataPoint
        fields = ['x_data_type', 'y_data_type', 'x', 'y']
        

class DataSerializer(serializers.ModelSerializer):
    data = MetricDataPointSerializer()

    class Meta:
        model = models.MetricDataPoint
        fields = ['user_id', 'data']



    def create(self, validated_data):
        user_id=validated_data['user_id']
        x_data_type=validated_data['data']['x_data_type']
        y_data_type=validated_data['data']['y_data_type']
        for object in validated_data['data']['x']:
            models.MetricDataPoint.objects.update_or_create(defaults=dict(
                user_id=user_id,
                data_type=x_data_type,
                date=object['date']),
                value=object['value']
                )
        for object in validated_data['data']['y']:
            models.MetricDataPoint.objects.update_or_create(defaults=dict(
                user_id=user_id,
                data_type=y_data_type,
                date=object['date']),
                value=object['value']
                )
        return validated_data




class GetDataSerializer(serializers.Serializer):
    data = MetricDataPointSerializer()

    class Meta:
        model = models.MetricDataPoint
        fields = ['user_id', 'data']