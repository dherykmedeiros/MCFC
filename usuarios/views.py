from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import NewUser
from .forms import UserRegisterForm
from django.urls import reverse_lazy

# Create your views here.
class UserListView(ListView):
  model = NewUser
  template_name = 'usuarios/users.html'
  context_object_name = 'users'

class UserDetailView(DetailView):
  model = NewUser
  template_name = 'usuarios/user_detail.html'
  context_object_name = 'user'
  slug_field = 'username'

class UserCreateView(CreateView):
  model = NewUser
  form_class = UserRegisterForm
  template_name = 'usuarios/user_create.html'
  success_url = reverse_lazy('users')

class UserUpdateView(UpdateView):
  model = NewUser
  template_name = 'usuarios/user_update.html'
  fields = ['username', 'first_name','last_name','posicao','descricao']
  success_url = reverse_lazy('users')

class UserDeleteView(DeleteView):
  model = NewUser
  template_name = 'usuarios/user_delete.html'
  success_url = reverse_lazy('users')



