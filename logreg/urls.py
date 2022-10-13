from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login , name= 'login'),
    path('signup', views.signup, name = 'signup'),
    path('logout', views.logout, name = 'logout'),
    path('create', views.create, name='create'),
    path('like/<str:id>' , views.like , name='like'),
]