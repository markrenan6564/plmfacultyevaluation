from django.urls import path
from . import views

app_name = "interface"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('signup/', views.signup, name="signup"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('evaluate/', views.evaluate, name="evaluate"),
]