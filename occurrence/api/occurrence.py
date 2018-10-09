from ..models import Occurrence
from rest_framework import viewsets, serializers
from rest_framework.permissions import AllowAny
from django_filters import rest_framework


class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = '__all__'


class OccurrenceViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = OccurrenceSerializer
    model = Occurrence
    http_method_names = ['get', 'head']
    filter_backends = (rest_framework.DjangoFilterBackend,)

    def get_queryset(self):
        return Occurrence.objects.all()
