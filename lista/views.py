from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from lista.models import ListaModel
from lista.serializers import ListaSerializer

class ListaViewSet(viewsets.ModelViewSet):
    queryset = ListaModel.objects.all()
    serializer_class = ListaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id','produto', 'adquirido']
