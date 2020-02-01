from django.test import TestCase
from customer.models import Customer
from insurance.models import Insurance
from contract.models import Contract

import faker
import logging

fake = faker.Faker("fr_FR")
logger = logging.Logger(__name__)


class ContractTestCase(TestCase):
    def setUp(self) -> None:
        customer = Customer.objects.create(
            name=fake.last_name(), first_name=fake.first_name(), age=30
        )

        insurance = Insurance.objects.create(name="MGEN")

        Contract.objects.create(
            insurance=insurance, customer=customer, signature_date="2020-02-01"
        )

    def test_contract(self):

        contract = Contract.objects.get(signature_date="2020-02-01")

        self.assertEqual(contract.status, "draft")
        self.assertEqual(contract.insurance.name, "MGEN")
        self.assertEqual(contract.customer.age, 30)

    def test_open_contract(self):

        contract = Contract.objects.get(signature_date="2020-02-01")

        contract.open()
        self.assertEqual(
            contract.status, "draft"
        )  # doit passer par l'étape pending avant son ouverture
        self.assertEqual(contract.is_mode_draft, True)

        contract.pending()
        self.assertEqual(contract.status, "pending")

        contract.open()
        self.assertEqual(contract.status, "open")  # là ouverture est possible
        self.assertEqual(contract.is_mode_open, True)
