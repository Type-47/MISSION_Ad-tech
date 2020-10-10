from rest_framework import serializers

from user_management.models import User_Info


class User_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = ('userid', 'time', 'referrer', 'count')
