from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    nome_completo = models.CharField(max_length=100,verbose_name='Nome Completo',null=True)
    telefone = models.CharField(max_length=16,null=True)
    cpf = models.CharField(max_length=14,verbose_name='CPF')
    user = models.OneToOneField(User,on_delete=models.CASCADE)

# Create your models here.
