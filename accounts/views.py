from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.models import User


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('core:home')


class UserLogoutView(LogoutView):
    next_page = 'core:home'


class UserDetailView(DetailView):
    model = User
    template_name = 'accounts/user_detail.html'
