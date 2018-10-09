from rest_framework import routers
from .occurrence import OccurrenceViewSet

router = routers.SimpleRouter()

router.register(r'occurrence', OccurrenceViewSet, 'occurrence')