from uuid import uuid4

from django.db import models


class myform(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    mobilenumber = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name
