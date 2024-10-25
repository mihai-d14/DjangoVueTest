from rest_framework import serializers

class MultiplicationSerializer(serializers.Serializer):
    value1 = serializers.FloatField()
    value2 = serializers.FloatField()