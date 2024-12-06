
from django.contrib import admin
from django.urls import path, include
from usuarios import urls
from django.conf.urls.static import static
from django.conf import settings 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(urls)),
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
