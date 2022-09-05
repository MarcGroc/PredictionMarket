from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from .forms import UserRegisterForm, UserLoginForm, UserPasswordResetForm


class UserRegisterView(CreateView, SuccessMessageMixin):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    def get_success_url(self):
        return reverse('home')


class UserLoginView(LoginView, SuccessMessageMixin):
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')
    authentication_form = UserLoginForm
    success_message = "You are logged in successfully"


class UserLogoutView(LogoutView, SuccessMessageMixin):
    template_name = 'users/logout.html'
    success_message = "You are logged out successfully"


class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    form_class = UserPasswordResetForm
    email_template_name = 'users/password_reset_email.html'


@method_decorator(login_required, name='dispatch')
class UserProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'

    def get_object(self, *args, **kwargs):
        return self.request.user
