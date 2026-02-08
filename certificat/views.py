from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Certificat
from .serializers import CertificatSerializer

class CertificatViewSet(viewsets.ModelViewSet):
    queryset = Certificat.objects.all()
    serializer_class = CertificatSerializer
