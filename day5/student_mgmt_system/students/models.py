import uuid
from django.db import models
from .utils import generate_index_number

class Student(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    index_number = models.CharField(max_length=10, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Only generate index_number if not set
        if not self.index_number:
            self.index_number = generate_index_number(self.full_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.index_number})"
