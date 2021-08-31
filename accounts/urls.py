from django.urls import path
import accounts.views

app_name = 'accounts'

urlpatterns = [
    path('login/', accounts.views.UserLoginView.as_view(), name='login'),
    ]
