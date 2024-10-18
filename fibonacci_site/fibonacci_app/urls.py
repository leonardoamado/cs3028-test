from django.urls import path
from . import views

urlpatterns = [
    path('', views.fibonacci_view, name='fibonacci'),
]