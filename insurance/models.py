from django.db import models


class Insurance(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Assurance"
        verbose_name_plural = "Assurances"
        ordering = ("name",)
