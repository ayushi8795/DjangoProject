from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signUp, name='signup'),
    path('login/', views.login, name='login'),
    path('users/', views.getAllUsers, name='get_all_users'),
    path('user/<str:email>/', views.userByEmail, name='user_by_email'),
    path('user/delete/<str:email>/', views.deleteUser, name='delete_user'),
    path('user/update/<str:email>/', views.updateUser, name='update_user'),
]   