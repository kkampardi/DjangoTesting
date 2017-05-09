from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import  Entry


class HomeView(TemplateView):

    template_name = 'index.html'
    queryset = Entry.objects.order_by('-created_at')

