from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *


def show_main_page(request):
    return render(request, template_name='index.html', context={})


def lk(request):
    return render(request, template_name='lk.html', context={})


def logout_user(request):
    logout(request)
    return redirect('foodsite:index')


def order(request):
    return render(request, template_name='order.html', context={})


def show_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id).prefetch_related('ingredients')

    return render(request, template_name='card.html', context={})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('foodsite:auth')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('foodsite:lk')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'auth.html'
