from django.db import models
from django.urls import reverse


class Eventos(models.Model):
    evento = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    data = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.evento} {self.local} ({self.data})"

    def get_absolute_url(self):
        return reverse('eventos_detail', args=[str(self.id)])

