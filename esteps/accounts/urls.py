from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
     path('getprofile', views.get_profile, name='get_profile'),
path('change_location', views.change_location, name='change_location'),
path('get_location', views.get_location, name='get_location'),
path('get_account_details', views.get_account_details, name='get_account_details'),

]