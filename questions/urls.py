from django.urls import path
from .views import QuestionView, AnswerView, user_ball_view

urlpatterns = [
    path('questions/', QuestionView.as_view(), name='question-list'),
    path('submit-answer/', AnswerView.as_view(), name='submit-answer'),
    path('user/ball/', user_ball_view, name='user_ball'),
]
