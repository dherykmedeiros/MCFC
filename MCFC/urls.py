from django.contrib import admin
from django.urls import path, include
from usuarios import urls
from jogadores import urls as urls_jogadores
from jogos import urls as urls_jogos
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from usuarios.views import logout_view
from .views import IndexView, administrativo
from django.contrib.auth.decorators import login_required, user_passes_test


def is_admin(user):
    return user.groups.filter(name="administrativo").exists()


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include(urls)),
    path(
        "login/", LoginView.as_view(template_name="usuarios/login.html"), name="login"
    ),
    path("logout/", logout_view, name="logout"),
    path("jogadores/", include(urls_jogadores)),
    path("jogos/", include(urls_jogos)),
    path("", IndexView.as_view(), name="home"),
    path("administrativo/", administrativo, name="administrativo"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
