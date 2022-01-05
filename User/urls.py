from django.urls import path
from . import views

app_name = 'User'
 
urlpatterns = [
    path('', views.Posts_list, name='posts'),
    path('create/', views.Create, name='create'),
    
]
