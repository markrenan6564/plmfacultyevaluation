from django.urls import path
from .views import RoomView
from . import views


urlpatterns = [
    path('room', RoomView.as_view()),
]
 
