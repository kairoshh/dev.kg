from apps.vacancy.views import VacancyView, VacancyDescriptionView
from django.urls import path

from rest_framework_simplejwt.views import(
    TokenObtainPairView,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Vacncy', VacancyView)
router.register('VacancyDescription', VacancyDescriptionView )
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    

]

urlpatterns += router.urls