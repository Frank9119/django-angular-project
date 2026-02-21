import uuid
from django.db import models




## Basemodel
class BaseModel(models.Model):
    primary_key = models.AutoField(primary_key=True)
    unique_id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True