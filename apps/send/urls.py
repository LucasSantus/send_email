from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    # path("send/", send_email, name="send"),

    # VALIDAÇÃO
    path("validacao/", validacao, name="validacao"),
]