from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('accounts/profile/',views.ProfileView.as_view(),name='profile'),
    path('accounts/profile-<int:pk>/update/',views.ProfileUpdateView.as_view(),name='profile-update'),
    path('accounts/login/',LoginView.as_view(),name='login'),
    path("accounts/register/",views.RegisterView.as_view(),name='register'),
    path('accounts/logout/',views.LogoutView.as_view(),name='logout'),
]
