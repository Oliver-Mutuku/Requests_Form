from django.urls import path, include
from .views import RequestViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"requests", RequestViewset)

urlpatterns = [
    path('', include(router.urls))   
]