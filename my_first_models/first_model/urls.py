from django.urls import path
from first_model import views

urlpatterns = [
    path("", views.home, name = 'home'),
]