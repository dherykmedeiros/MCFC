from django.urls import path
from .views import UserCreateView, UserListView, UserDetailView, UserUpdateView, UserDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('', UserListView.as_view(), name='users'),
    path('detail/<int:pk>/', login_required(UserDetailView.as_view()), name='user_detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
