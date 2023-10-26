from django.urls import path
from . import views

app_name = "interface"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name="profile"),
    path('evaluate/', views.evaluate, name="evaluate"),
    path('evaluate/manual', views.manual_add, name="manual_add"),
    path('evaluate/success', views.duga, name="duga"),
]