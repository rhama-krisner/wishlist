from rest_framework import serializers
from lista.models import ListaModel

class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaModel
        fields = '__all__'



