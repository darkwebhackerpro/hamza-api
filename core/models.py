from django.db import models
import uuid
SEMESTER_CHOICES = (("Admin", "0"),("User", "1"),)


class Employ(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    department = models.CharField(max_length=200)
    api_key = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    admin_privilage = models.CharField(max_length=20, choices=SEMESTER_CHOICES, default='1')