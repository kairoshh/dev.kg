from apps.events.views import EventView
from django.urls import path

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('event', EventView)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]

urlpatterns += router.urls