from rest_framework import serializers
from .models import Job




class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('primary_key', 'title', 'description', 'salary', 'created_at')
        read_only_fields = ('owner',)


