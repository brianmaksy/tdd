import uuid
from django.db import models
from django.contrib import auth 

auth.signals.user_logged_in.disconnect(auth.models.update_last_login)

class User(models.Model):
    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = [] # no need req fields because only one field. If absent, entry won't be created. 
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True

class Token(models.Model):
    email = models.EmailField() # auto gen? need be non nul?
    uid = models.CharField(default=uuid.uuid4, max_length=40)
