from django.shortcuts import render, get_object_or_404

from .models import Dish


def show_main_page(request):
    return render(request, template_name='index.html', context={})


def auth(request):
    return render(request, template_name='auth.html', context={})


def registration(request):
    return render(request, template_name='registration.html', context={})


def lk(request):
    return render(request, template_name='lk.html', context={})


def order(request):
    return render(request, template_name='order.html', context={})


def show_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id).prefetch_related('ingredients')

    return render(request, template_name='card.html', context={})
