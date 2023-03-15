from django.shortcuts import render


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
