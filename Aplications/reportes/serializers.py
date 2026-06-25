from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'description', 'address', 'latitude', 'longitude', 'picture', 'creation_date', 'update_date']
        read_only_fields = ('creation_date', 'update_date')

    def validate_picture(self, value):
        # Validar que la imagen no sea mayor a 2MB
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("La imagen no puede superar los 2MB")
        return value
        
    def validate_latitude(self, value):
        # Validar que la latitud esté entre -90 y 90
        if not -90 <= value <= 90:
            raise serializers.ValidationError("La latitud debe estar entre -90 y 90")
        return value
    
    def validate_longitude(self, value):
        # Validar que la longitud esté entre -180 y 180
        if not -180 <= value <= 180:
            raise serializers.ValidationError("La longitud debe estar entre -180 y 180")
        return value

    def validate(self, attrs):
        # Validar que la imagen sea una imagen
        if not attrs['picture'].content_type.startswith('image'):
            raise serializers.ValidationError("La imagen debe ser una imagen")
        return attrs

    def create(self, validated_data):
        report = Report.objects.create(**validated_data)
        return report
    
    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.address = validated_data.get('address', instance.address)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return {"message": "Reporte eliminado exitosamente"}    

    