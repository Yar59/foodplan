from django.urls import path

from .views import show_main_page

app_name = 'foodsite'

urlpatterns = [
    path('', show_main_page, name='index')
]