from rest_framework import routers
from .views import CertificatViewSet

router = routers.DefaultRouter()
router.register(r'certificats', CertificatViewSet)

urlpatterns = router.urls
