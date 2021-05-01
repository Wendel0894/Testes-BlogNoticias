
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.

class CadastroPageView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'cadastro.html'

# CRUD de usuários

class ManageUsersPageView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/manage.users.html'
    context_object_name = 'usuarios'

class DetailUserPageView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/detail_user.html'
    context_object_name = 'usuario'

class AddUserPageView(LoginRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'users/add_user.html'
    success_url = reverse_lazy('manage_users')

class EditUserPageView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('manage_users')
    template_name = 'users/edit_user.html'
    fields = ['username', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_active']

class DeleteUserPageView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('manage_users')










