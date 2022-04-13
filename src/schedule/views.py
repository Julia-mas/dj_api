from rest_framework import viewsets, permissions
from .models import Schedule
from .serializers import ScheduleSerializer


class ScheduleView(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScheduleSerializer
