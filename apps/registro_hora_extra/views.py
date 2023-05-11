from django.shortcuts import render
from .models import RegistroHoraExtra

from django.views.generic import ListView


class HoraExtraList(ListView):
    model = RegistroHoraExtra

