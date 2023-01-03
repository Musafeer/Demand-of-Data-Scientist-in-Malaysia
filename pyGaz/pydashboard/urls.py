from django.urls import path, include
from . import views
from .views import Chart

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView, name="home"),
    path('test2/', views.dashboardView, name="test2"),
    path('login/', LoginView.as_view(next_page='test2'), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='home'), name="logout"),
    path("test2/",Chart,name="Chart"),
    
]
