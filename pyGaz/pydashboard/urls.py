from django.urls import path, include
from . import views
from .views import Chart

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView, name="home"),
    path('testDashboard/', views.dashboardView, name="testDashboard"),
    path('login/', LoginView.as_view(next_page='testDashboard'), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='home'), name="logout"),
    # path('',include('pyGaz.urls'))
    path("testDashboard/",Chart,name="Chart")
    
]
