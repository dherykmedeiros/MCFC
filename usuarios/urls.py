from django.urls import path
from .views import UserCreateView, UserListView, UserDetailView, UserUpdateView, UserDeleteView
from django.contrib.auth.decorators import login_required,user_passes_test
from .decorators import can_edit_info

def is_admin(user):
  return user.groups.filter(name='administrativo').exists()


urlpatterns = [
    path('create/', login_required(user_passes_test(is_admin)(UserCreateView.as_view())), name='user_create'),
    path('', login_required(user_passes_test(is_admin)(UserListView.as_view())), name='users'),
    path('detail/<uuid:id>/', login_required(can_edit_info(UserDetailView.as_view())), name='user_detail'),
    path('update/<uuid:id>/', login_required(can_edit_info(UserUpdateView.as_view())), name='user_update'),
    path('delete/<uuid:id>/', login_required(user_passes_test(is_admin)(UserDeleteView.as_view())), name='user_delete'),
]
