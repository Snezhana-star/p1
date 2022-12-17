from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateView

from .models import Order


class Index(TemplateView):
    template_name = 'index.html'


class Orders(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'orders'


class About(TemplateView):
    template_name = 'about.html'


class Contacts(TemplateView):
    template_name = 'contacts.html'


class CreateOrder(LoginRequiredMixin, CreateView):
    template_name = 'createorder.html'
    model = Order
    login_url = '/login'
    success_url = '/order'


class Login(LoginView):
    template_name = 'login.html'
    model = User
    success_url = '/'
