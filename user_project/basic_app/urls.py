from django.contrib import admin
from django.urls import path,include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('login_page/',views.login_page,name='login_page'),

]
