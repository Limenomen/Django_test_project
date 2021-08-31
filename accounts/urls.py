from django.urls import path
import accounts.views


app_name = 'accounts'

urlpatterns = [
    path('login/', accounts.views.UserLoginView.as_view(), name='login'),
    path('logout/', accounts.views.UserLogoutView.as_view(), name='logout'),
    path('register/', accounts.views.UserLoginView.as_view(), name='register'),
    path('<int:pk>/', accounts.views.UserDetailView.as_view(), name='user_detail'),
]
