
from django.urls import path
from api.views import Viewinstallations, Viewstatus
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    'installations',Viewinstallations, basename= 'installation',

)
router.register(
    'status',Viewstatus, basename= 'status',

)

urlpatterns = router.urls