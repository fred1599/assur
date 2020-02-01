import json

from datetime import date

from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from contract.models import Contract
from insurance.models import Insurance
from customer.models import Customer


@csrf_exempt
def create_contract(request):
    if request.method == "POST":
        response = json.loads(request.body.decode("utf8"))
        if "customer" not in response or "insurance" not in response:
            data = {
                "success": False,
                "error": "missing informations customer or insurances",
            }
            return HttpResponse(JsonResponse(data))

        customer_name = response["customer"]["name"]
        customer_firstname = response["customer"]["first_name"]
        customer_age = response["customer"]["age"]
        customer = Customer.objects.create(
            name=customer_name, first_name=customer_firstname, age=customer_age
        )

        insurance_name = response["insurance"]
        insurance = Insurance.objects.create(name=insurance_name)

        contract = Contract.objects.create(
            customer=customer, insurance=insurance, signature_date=date.today()
        )

        contract.number = "C{}".format(contract.pk)
        contract.save(update_fields=["number", "signature_date"])

        data = {
            "contract": {
                "number": contract.number,
                "customer": customer.name + " " + customer.first_name,
                "insurance": insurance.name,
            }
        }

        return HttpResponse(JsonResponse(data))
