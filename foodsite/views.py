from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *


def show_main_page(request):
    return render(request, template_name='index.html', context={})


@login_required
def lk(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен.')
            return redirect('foodsite:lk')
    else:
        user_form = UserProfileForm(instance=request.user)
    return render(request, template_name='lk.html', context={'user_form': user_form})


def logout_user(request):
    logout(request)
    return redirect('foodsite:index')


@login_required
def order(request):
    return render(request, template_name='order.html', context={})


def show_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id).prefetch_related('ingredients')

    return render(request, template_name='card.html', context={})


@login_required
def show_menu(request):
    return render(request, template_name='menu.html', context={})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('foodsite:auth')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('foodsite:order')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'auth.html'
