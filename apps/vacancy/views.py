from apps.vacancy.serializers import VacancySerializer, VacancyDescriptionSerializer

from apps.vacancy.models import Vacancy, VacancyDescription


from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class VacancyView(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = (IsAuthenticated,)

class VacancyDescriptionView(ModelViewSet):
    queryset = VacancyDescription.objects.all()
    serializer_class = VacancyDescriptionSerializer
    permission_classes = (IsAuthenticated,)


