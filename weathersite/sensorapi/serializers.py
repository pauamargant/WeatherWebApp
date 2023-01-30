from rest_framework import serializers
from sensordata.models import Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ('value', 'unit', 'sensor')
