from django.urls import path
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
    path("login/", views.Login, name="login"),
    path("register/", views.Register, name="register"),
    path(
        "password_reset/",
        auth.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        auth.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        auth.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "logout/",
        auth.LogoutView.as_view(template_name="classroom/index.html"),
        name="logout",
    ),
    path("profile/", views.Profile, name="profile"),
    # path("Profile_update/", users.Profile_update, name="Profile_update"),
]
