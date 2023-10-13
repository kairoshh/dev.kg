from apps.company_info.views import CompanyView
from django.urls import path

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('company', CompanyView)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]

urlpatterns += router.urls