from django.urls import path
from . import views


app_name = 'user'
urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('register_user',views.register_user, name='register_user'),
    path('after_login',views.after_login, name='after_login'),


    
]
