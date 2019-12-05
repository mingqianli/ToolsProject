
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from . import views

urlpatterns = [
        path('map/',views.all),
    ]


