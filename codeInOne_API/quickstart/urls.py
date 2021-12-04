from django.urls import path
from .views import ChallengeViews

urlpatterns = [
    path('challenges/', ChallengeViews.as_view()),
    path('challenges/<int:id>', ChallengeViews.as_view())
]