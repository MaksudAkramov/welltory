from rest_framework import serializers

from user import models

class AccountSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        
        user = models.Account.objects.create_user(**validated_data)
        return user

    class Meta:
        
        model = models.Account
        fields = ['username', 'email', 'password', 'is_staff']