from django.urls import path, include
from .views import RequestViewset, ApprovalViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"requests", RequestViewset)
router.register(r"approval", ApprovalViewset)

urlpatterns = [
    path('', include(router.urls))
]

# The URLs will be automatically generated as:
# /requests/ - list view
# /requests/<id>/ - detail view
# /requests/<id>/admin_view/ - admin view for a specific request
# /requests/<id>/process/ - endpoint to process a request