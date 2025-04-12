from django.urls import path, include
from .views import RequestViewset, ApprovalViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"requests", RequestViewset)
router.register(r"approval", ApprovalViewset)

urlpatterns = [
    path('', include(router.urls))
]