from django.urls import path

from .views import show_main_page, auth, registration, lk, order, show_dish

app_name = 'foodsite'

urlpatterns = [
    path('', show_main_page, name='index'),
    path('auth/', auth, name='auth'),
    path('registration/', registration, name='registration'),
    path('lk/', lk, name='lk'),
    path('order/', order, name='order'),
    path('dish/<dish_id>/', show_dish, name='dish'),
]