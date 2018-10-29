from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('sobre', views.Markdown.as_view(), {'slug': 'sobre'}),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='website/password_reset_form.html'
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done',
        auth_views.PasswordResetDoneView.as_view(
            template_name='website/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'password_reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='website/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'password_reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='website/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]
