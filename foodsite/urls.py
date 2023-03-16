from django.urls import path

from .views import show_main_page, lk, order, show_dish, logout_user, RegisterUser, LoginUser

app_name = 'foodsite'

urlpatterns = [
    path('', show_main_page, name='index'),
    path('auth/', LoginUser.as_view(), name='auth'),
    path('logout/', logout_user, name='logout'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('lk/', lk, name='lk'),
    path('order/', order, name='order'),
    path('dish/<dish_id>/', show_dish, name='dish'),
]