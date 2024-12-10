from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import NewUser, Invitation
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
class UserListView(ListView):
  model = NewUser
  template_name = 'usuarios/users.html'
  context_object_name = 'users'

class UserDetailView(DetailView):
  model = NewUser
  template_name = 'usuarios/user_detail.html'
  context_object_name = 'user'
  pk_url_kwarg = 'id'
  slug_field = 'username'

class UserCreateView(CreateView):
  model = NewUser
  form_class = UserRegisterForm
  template_name = 'usuarios/user_create.html'
  success_url = reverse_lazy('users')

class UserUpdateView(UpdateView):
  model = NewUser
  template_name = 'usuarios/user_update.html'
  pk_url_kwarg = 'id'
  fields = ['username', 'first_name','last_name','posicao','descricao','foto_perfil']
  success_url = reverse_lazy('users')

class UserDeleteView(DeleteView):
  model = NewUser
  template_name = 'usuarios/user_delete.html'
  pk_url_kwarg = 'id'
  success_url = reverse_lazy('users')

@login_required
def logout_view(request):
  logout(request)
  return redirect('login')

def send_invitation(email):
    # Criar o token
    invitation = Invitation.objects.create(email=email)
    
    # Gerar o link único
    link = f"http://127.0.0.1:8000/users/create{invitation.token}/"
    
    # Enviar por e-mail
    send_mail(
        subject="Convite para cadastro",
        message=f"Use este link para se cadastrar: {link}",
        from_email="mcfc@mcfc.com",
        recipient_list=[email],
    )
    return link

