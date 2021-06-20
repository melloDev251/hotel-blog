from django.urls import path
from .views import login_hotel, register, logout_hotel
urlpatterns = [
    path("login", login_hotel, name="login-hotel1"),
    path("register", register, name="register1"),
    path("logout", logout_hotel, name="logout1"),
]