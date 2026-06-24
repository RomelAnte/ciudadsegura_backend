from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'description', 'address', 'latitude', 'longitude', 'picture', 'creation_date', 'update_date']

    