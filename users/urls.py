
from django.urls import path
from .views import (
    CadastroPageView,
    ManageUsersPageView,
    AddUserPageView,
    EditUserPageView,
    DetailUserPageView,
    DeleteUserPageView
)

urlpatterns = [
    path('Cadastrar/', CadastroPageView.as_view(), name = 'cadastro'),
    path('Gerenciar/', ManageUsersPageView.as_view(), name = 'manage_users'),
    path('Adicionar/', AddUserPageView.as_view(), name = 'add_user'),
    path('Editar/<int:pk>/', EditUserPageView.as_view(), name = 'edit_user'),
    path('Visualizar/<int:pk>/', DetailUserPageView.as_view(), name = 'detail_user'),
    path('Deletar/<int:pk>/', DeleteUserPageView.as_view(), name = 'delete_user')


]