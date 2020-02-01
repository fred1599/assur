from django.db import models

from customer.models import Customer
from insurance.models import Insurance


class Contract(models.Model):
    """
    Les statuts d'un contrat
      - draft (mode brouillon avec possibilité de modification sans créer un avenant)
      - pending (mode intermédiaire entre brouillon et ouvert)
      - open (mode ouvert, modification possible qu'en créant un avenant)
      - closed (mode clos, contrat inutilisable, juste dans l'historique)

    number: représente le numéro du contrat
    """

    STATUSES = (
        ("draft", "Brouillon"),
        ("pending", "En attente"),
        ("open", "Ouvert"),
        ("closed", "Clos"),
    )

    status = models.CharField(
        "Status", max_length=7, choices=STATUSES, default="draft", db_index=True
    )

    number = models.CharField(
        max_length=20, unique=True, editable=False, null=False, db_index=True
    )

    signature_date = models.DateField(
        verbose_name="Date de souscription", null=False, blank=False
    )

    insurance = models.ForeignKey(
        verbose_name="Assurance",
        to=Insurance,
        related_name="insurer_contract_set",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    customer = models.ForeignKey(
        verbose_name="Adhérent",
        to=Customer,
        related_name="customer_contract_set",
        db_index=True,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    def open(self):
        if self.status == "pending":
            self.status = "open"

    def pending(self):
        if self.status == "draft":
            self.status = "pending"

    def close(self):
        if self.status == "open":
            self.status = "closed"

    @property
    def is_mode_draft(self):
        return self.status == "draft"

    @property
    def is_mode_open(self):
        return self.status == "open"

    @property
    def is_mode_closed(self):
        return self.status == "closed"

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        self.number = "C{}".format(self.pk)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Contrat"
        verbose_name_plural = "Contrats"
        ordering = ("signature_date", "number")
