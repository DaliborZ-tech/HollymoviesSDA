from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView

from accounts.forms import SignUpForm


class SignUpView(CreateView):
    template_name = "form.html"
    form_class = SignUpForm
    success_url = "/accounts/login/"
