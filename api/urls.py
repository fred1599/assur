from django.urls import path
from api.views import create_contract

urlpatterns = [path("v1/contract/create/", create_contract)]
