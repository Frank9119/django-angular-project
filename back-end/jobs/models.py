from django.db import models
from django.conf import settings
from mixin.models import BaseModel


# Create your models here.
class Job(BaseModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title}-{self.salary}"
    
    class Meta:
        verbose_name = 'job'
        verbose_name_plural = 'jobs'
        ordering = ['-primary_key']