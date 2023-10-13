from apps.organizations.views import OrganizationView
from django.urls import path

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('organization', OrganizationView)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]

urlpatterns += router.urls