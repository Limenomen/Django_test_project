from django.urls import path, include
import core.views

urlpatterns = [
    path('', core.views.index),
]