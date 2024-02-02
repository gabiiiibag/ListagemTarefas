from django.db import models
from datetime import date

# Create your models here.
class toDo(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    entrega = models.DateField(verbose_name="Entrega", null=False, blank=False)
    finalizacao = models.DateField(null=True)

    class Meta:
        ordering = ["entrega"]

    def completed(self):
        if not self.finalizacao:
            self.finalizacao = date.today()
            self.save()

