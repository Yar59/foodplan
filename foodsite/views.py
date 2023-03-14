from django.shortcuts import render


def show_main_page(request):
    return render(request, template_name='index.html', context={})