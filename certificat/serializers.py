from rest_framework import serializers
from .models import Certificat

class CertificatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificat
        fields = '__all__'
