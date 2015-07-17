from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    company_name = models.CharField("Razon Social",max_length=100)
    def __str__(self):              # __unicode__ on Python 2
        return self.company_name

class Navigation(models.Model):
    item_name = models.CharField("Nombre",max_length=100)
    parent    = models.ForeignKey('self', null=True, blank=True, related_name='submenu')
    description = models.CharField("Descripcion",max_length=254)
    url = models.CharField("Url",max_length=254)
    def __str__(self):              # __unicode__ on Python 2
        return self.item_name

class ProfileCompany(models.Model):
    profile_name = models.CharField("Perfil",max_length=100)
    company = models.ForeignKey(Company)
    def __str__(self):              # __unicode__ on Python 2
        return '%s %s' % (self.company.company_name, self.profile_name)

class UserCompany(models.Model):
    company = models.ForeignKey(Company)
    user =  models.ForeignKey(User)

    def __str__(self):              # __unicode__ on Python 2
        return '%s %s' % (self.company.company_name, self.user.username)
#        user = models.ManyToManyField(User,blank=True)

