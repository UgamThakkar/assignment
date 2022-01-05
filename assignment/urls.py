from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('User.urls')),
    path('login/', views.login_view, name='login'),
    path('', views.register, name='register'),
]   

