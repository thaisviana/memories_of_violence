from ..models import Occurrence
from rest_framework import viewsets, serializers
from rest_framework.permissions import AllowAny
from django_filters import rest_framework


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        from ..models import Asset
        model = Asset
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        from ..models import Location
        model = Location
        fields = '__all__'


class OccurrenceSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    approximatedRangeDate = serializers.SerializerMethodField()
    asset_set = AssetSerializer(many=True)

    class Meta:
        model = Occurrence
        exclude = ('startDate', 'finishDate',)

    def get_approximatedRangeDate(self, obj):
        return {'startDate': obj.startDate, 'finishDate': obj.finishDate}


class OccurrenceViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = OccurrenceSerializer
    model = Occurrence
    http_method_names = ['get', 'head']
    filter_backends = (rest_framework.DjangoFilterBackend,)

    def get_queryset(self):
        return Occurrence.objects.all()
