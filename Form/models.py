from django.db import models

class List(models.Model):
    nombre = models.CharField(primary_key=True, max_length=60, blank=False)
    numero = models.IntegerField(null=True, blank=True, verbose_name ='número')

    def publish(self):
        self.save()

    def __str__(self):
        return self.nombre
