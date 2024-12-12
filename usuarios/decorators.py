from functools import wraps
from django.shortcuts import redirect


def can_edit_info(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Verifica se é um administrador
        if request.user.groups.filter(name="administrativo").exists():
            return view_func(request, *args, **kwargs)
        # Verifica se o usuário logado está acessando suas próprias informações
        if request.user.id == kwargs.get("id"):
            return view_func(request, *args, **kwargs)
        # Caso contrário, retorna Forbidden
        return redirect("home")

    return _wrapped_view
