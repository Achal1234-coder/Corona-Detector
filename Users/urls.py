from django.urls import path
from . import views

app_name = 'Users'

urlpatterns = [

    path('', views.home_view, name="home"),
    path('LogOut', views.log_out_view, name="LogOut"),
    path('detect', views.detect, name='detect')
]