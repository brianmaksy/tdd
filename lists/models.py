from django.db import models
from django.core.urlresolvers import reverse 

class List(models.Model):
    
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id]) # essentially does the reverse of what Django normally does with urls.py (see the docs)

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
