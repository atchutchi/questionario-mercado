from django.db import models

class IndicadorBase(models.Model):
    OPERADORA_CHOICES = [
        ('orange', 'Orange'),
        ('mtn', 'MTN'),
    ]
    
    ano = models.IntegerField()
    mes = models.IntegerField(choices=[(i, i) for i in range(1, 13)])
    operadora = models.CharField(
        max_length=10,
        choices=OPERADORA_CHOICES,
        verbose_name="Operadora",
        null=True,  # Permite valores nulos temporariamente
        blank=True  # Permite valores em branco temporariamente
    )

    class Meta:
        abstract = True