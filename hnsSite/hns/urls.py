from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('services/', views.services_list, name='services_list'),
    path('becomeContractor/', views.becomeContractor, name='becomeContractor'),
    path('login/', views.login, name='login'),
    path('create_account/', views.createUserAccount, name="createUserAccount"),
    path('user_profile/', views.userProfile, name="userProfile"),
]