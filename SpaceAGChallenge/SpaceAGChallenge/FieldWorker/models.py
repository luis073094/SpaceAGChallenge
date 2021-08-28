import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class FieldWorker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    function = models.TextField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True
        db_table = 'field_worker'