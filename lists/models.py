from django.db import models
from django.core.urlresolvers import reverse 

class List(models.Model):
    
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id]) # essentially does the reverse of what Django normally does with urls.py (see the docs)

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
    
    # meta as in metadata?! https://stackoverflow.com/questions/10344197/how-does-djangos-nested-meta-class-work 
    # see second answer 
    class Meta:
        unique_together = ('list', 'text')