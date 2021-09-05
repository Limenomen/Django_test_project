from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView
from django.urls import reverse
from django.contrib.auth.models import User
import accounts.forms
from django.contrib.auth import login


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


class UserRegisterView(CreateView, TittleMixin):
    title = 'Регистрация'
    form_class = accounts.forms.UserRegistrationForm
    template_name = 'accounts/register_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:home')
        return super(UserRegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return reverse('core:home')


class UserDetailView(TittleMixin, DetailView):
    title = 'Профиль'
    model = User
    template_name = 'accounts/user_detail.html'
