from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    # INDEX
    path("", index, name="index"),
]