from django.urls import path
from .views import *
urlpatterns = [
    path("", dashboard, name="dashboard1"),
    path("my-hotel", user_hotels, name="my-hotel1"),
    path("add-hotel", addHotel.as_view(), name="add-hotel1"),
    path("update-hotel/<int:pk>", updateHotel.as_view(), name="update-hotel1"),
    path("delete-hotel/<int:pk>", deleteHotel.as_view(), name="delete-hotel1"),
]