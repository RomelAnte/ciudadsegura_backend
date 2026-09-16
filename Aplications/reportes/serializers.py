from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Report, ReportType

class ReportSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Report
        fields = ['id', 'user', 'type', 'description', 'address', 'latitude', 'longitude', 'picture', 'status', 'creation_date', 'update_date']
        read_only_fields = ('user', 'creation_date', 'update_date')

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
        picture = attrs.get('picture')
        if picture and hasattr(picture, 'content_type'):
            if not picture.content_type.startswith('image/'):
                raise serializers.ValidationError({"picture": "El archivo debe ser una imagen"})
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ('id', 'username', 'email', 'first_name', 'last_name')

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise serializers.ValidationError("Credenciales incorrectas")
        return attrs
    
    def get_user(self):
        return User.objects.get(username=self.validated_data['username'])
    
    def get_token(self):
        return self.get_user().get_token()
    
    def get_token_refresh(self):
        return self.get_user().get_token_refresh()

class TipoReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportType
        fields = ['id', 'name', 'description', 'status', 'creation_date', 'update_date']
        read_only_fields = ('id', 'creation_date', 'update_date')



    