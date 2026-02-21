from .models import Job
from .serializers import JobSerializer
## rest framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Job.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
