from django.db import models

class Arbol(models.Model):
    nodo=models.IntegerField(primary_key=True)
    texto=models.CharField(max_length=100)
    pregunta=models.BooleanField(default=False)
    
    def __int__(self):
        return self.nodo

class Tarea(models.Model):
    tarea=models.CharField(max_length=100)
    
    def __str__(self):
        return self.tarea