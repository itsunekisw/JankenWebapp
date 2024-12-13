from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_view, name='top'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('janken/', views.janken_view, name='janken'),
    path('user/<int:id>/', views.user_view, name='user'),
    path('ranking/', views.ranking_view, name='ranking'),
]
