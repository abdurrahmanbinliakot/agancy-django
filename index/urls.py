from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = 'index' ),  
    path('signin', views.signin, name = 'signin' ),  
    path('UserLogout', views.UserLogout, name = 'UserLogout' ), 
    path('registration', views.registration, name = 'registration' ),
]