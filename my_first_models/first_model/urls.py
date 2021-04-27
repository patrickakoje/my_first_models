from django.urls import path
from .views import HomeView, ArticlesDetailsView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticlesDetailsView.as_view(), name="article-details")
]