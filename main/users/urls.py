from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.urls import path

from main.users import views
from main.users.views import send_verification_email, verify
from main.users.apps import UsersConfig
from main.users.views import RegisterView, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    path("", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('send_verification_email/', send_verification_email, name='send_verification_email'),
    path('verify/', verify, name='verify'),
]