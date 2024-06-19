# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home , name='home'),
    path('<int:info_id>/', views.detail_info , name='info')

]