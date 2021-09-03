from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth.models import User


class TittleMixin:
    title: str = None

    def get_title(self) -> str:
        return self.title

    def get_context_data(self, **kwargs):
        c = super().get_context_data()
        c['title'] = self.get_title()
        return c


class UserLoginView(TittleMixin, LoginView):
    title = 'Войти'
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('core:home')


class UserLogoutView(LogoutView):
    next_page = 'core:home'


class UserDetailView(TittleMixin, DetailView):
    title = 'Профиль'
    model = User
    template_name = 'accounts/user_detail.html'
