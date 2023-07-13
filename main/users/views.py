from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from main.users.forms import UserRegisterForm, UserProfileForm
from main.users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)
        return response


class PasswordResetCustomView(PasswordResetView):
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('users:password_reset_done')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user

