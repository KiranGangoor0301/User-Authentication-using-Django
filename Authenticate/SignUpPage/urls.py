
from django.contrib import admin
from django.urls import path
from SignUpPage import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]
