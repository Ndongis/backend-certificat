from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Certificat

class CertificatModelTest(TestCase):
    def setUp(self):
        self.cert = Certificat.objects.create(
            nom_habitant="John Doe",
            adresse="123 Rue DevOps",
            numero_certificat="C-001",
            statut_paiement="payé"
        )

    def test_certificat_creation(self):
        self.assertEqual(self.cert.nom_habitant, "John Doe")
        self.assertEqual(self.cert.numero_certificat, "C-001")
        self.assertEqual(self.cert.statut_paiement, "payé")
