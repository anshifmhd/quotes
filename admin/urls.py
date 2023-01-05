from django.urls import path
from . import views


app_name = 'admin'
urlpatterns = [
    path('add_admin',views.add_admin, name='add_admin'),
    path('index_admin',views.index_admin, name='index_admin'),
    path('view_quotes',views.view_quotes, name='view_quotes'),
    path('update_quotes/<int:idd>',views.update_quotes, name='update_quotes'),




]
