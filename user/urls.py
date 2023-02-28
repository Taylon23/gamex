from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserCreate, PerfilUpdate


urlpatterns = [
    path('singup/', UserCreate.as_view(), name="singup"),
    path('logout/', auth_views.LogoutView.as_view(), 'logout'),
    path('atualizar/perfil/', PerfilUpdate.as_view(), name="perfil-update"),
]
