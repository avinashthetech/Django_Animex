from django.urls import path
from . import views
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    # path('', views.home, name='home'),
    path('signout/', views.signout, name='signout'),
    path('register/', views.registration, name='register'),
    path('ch',views.ch,name="login"),
    path('',views.moive,name='moive'),
    path('carousel',views.car,name='carousel')
]
