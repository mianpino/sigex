from django.db import models
from app.models import Company

# Create your models here.
class Vendedor(models.Model):
    FirstName = models.CharField("Nombre",max_length=100)
    LastName  = models.CharField("Apellidos",max_length=100)
    company   = models.ForeignKey(Company)
    def __str__(self):              # __unicode__ on Python 2
        return '%s %s' % (self.FirstName, self.LastName)
