from django.urls import path
from . import  views

urlpatterns = [
    path('login/', views.loginPage, name = "login"),
    path('logout/',views.logoutUser, name = 'logout'),
    path('', views.profiles, name = "profiles"),
    path('profile/<str:pk>', views.userProfile, name = "userProfile")
]