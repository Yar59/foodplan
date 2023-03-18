from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import HttpResponseRedirect
from .forms import *
from .models import *


def show_main_page(request):
    dishes = Dish.objects.all()[:3]
    return render(request, template_name='index.html', context={'dishes': dishes})


@login_required
def lk(request):
    tariff = request.user.tarif
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен.')
            return redirect('foodsite:lk')
    else:
        user_form = UserProfileForm(instance=request.user)
    return render(request, template_name='lk.html', context={'user_form': user_form, 'tariff': tariff})


def logout_user(request):
    logout(request)
    return redirect('foodsite:index')


@login_required
def order(request):
    if request.method == 'POST':
        preferred_menu = request.POST.get('menu')
        term = request.POST.get('term')
        breakfast = request.POST.get('breakfast')
        lunch = request.POST.get('lunch')
        dinner = request.POST.get('dinner')
        dessert = request.POST.get('dessert')
        allergy = request.POST.get('allergy')
        tarif = Tarif.objects.create(
            preferred_menu=preferred_menu,
            allergy=allergy.split('|'),
            duration=term.split()[0],
            breakfast=breakfast,
            lunch=lunch,
            dinner=dinner,
            dessert=dessert,
        )
        return HttpResponseRedirect("/")
    return render(request, template_name='order.html', context={})


def show_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    ingredients_dish = dish.ingredients.all()
    return render(request, template_name='card.html', context={'dish':dish,
                                                               'ingredients_dish':ingredients_dish})


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
