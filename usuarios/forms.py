from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django import forms
from .models import NewUser

class UserRegisterForm(UserCreationForm):
  groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required= False
    )
  email = forms.EmailField()
  class Meta:
    model = NewUser
    fields = ['username','first_name','last_name', 'email', 'password1', 'password2','posicao','descricao','foto_perfil']
    widgets = {
            'username': forms.TextInput(attrs={
                'class': 'px-4 py-2 text-base text-gray-700 border border-gray-300 rounded-md',
                'placeholder': 'Digite seu nome de usuário'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'px-4 py-2 text-base text-gray-700 border border-gray-300 rounded-md',
                'placeholder': 'Digite seu primeiro nome'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'px-4 py-2 text-base text-gray-700 border border-gray-300 rounded-md',
                'placeholder': 'Digite seu sobrenome'
            }),
            'posicao': forms.Select(attrs={
                'class': 'px-4 py-2 text-base text-gray-700 border border-gray-300 rounded-md',
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'px-4 py-2 text-base text-gray-700 border border-gray-300 rounded-md',
                'placeholder': 'Digite uma descrição',
                'rows': 4,
            }),
        }
  email = forms.EmailField(
      widget=forms.EmailInput(attrs={
          'class': 'px-4 py-2 text-base text-gray-700 border border-gray-300 rounded-md',
          'placeholder': 'Digite seu email'
      })
  )
  password1 = forms.CharField(
      widget=forms.PasswordInput(attrs={
          'class': 'px-4 py-2 text-base text-gray-700 border border-gray-300 rounded-md',
          'placeholder': 'Digite sua senha'
      })
  )
  password2 = forms.CharField(
      widget=forms.PasswordInput(attrs={
          'class': 'px-4 py-2 text-base text-gray-700 border border-gray-300 rounded-md',
          'placeholder': 'Confirme sua senha'
      })
  )
