from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),

    path('verify/', views.verify, name='verify'),

    path('login_view/', views.login_view, name='log-in'),

    path('forgot_password/', views.forgot_password, name='forgot-password'),

    path('reset_password/', views.reset_password, name='reset-password'),
]
