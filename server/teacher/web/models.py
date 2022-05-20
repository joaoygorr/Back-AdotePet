from django.db import models

# Create your models here.
class Teacher(models.Model): 
    full_name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone = models.CharField(max_length=11, null=False, blank=False)
    neighborhood  = models.CharField(max_length=60, null=False, blank=False)
    number = models.IntegerField(null=False, blank=False)
    district = models.CharField(max_length=30, null=False, blank=False)
    complement = models.CharField(max_length=100, null=False, blank=True)
    zip_code = models.CharField(max_length=8, null=False, blank=False)
    state = models.CharField(max_length=2, null=False, blank=False)
    cod_ibge = models.IntegerField(null=False, blank=False)
    photo_user = models.ImageField(null=False)
