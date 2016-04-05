from __future__ import unicode_literals

from django.db import models

import uuid

# Create your models here.

class LoginModel(models.Model):
        uid = models.CharField(max_length=100, unique = True ,default = uuid.uuid4)
        Last_Name = models.CharField(max_length=45, default = None)
        EmailID = models.EmailField(default = None)
        SSN = models.CharField(max_length=4)
