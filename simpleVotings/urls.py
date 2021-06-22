from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'surveys'
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),

    path('surveys/delete/<int:pk>', SurveyDeleteView.as_view()),
    path('surveys/create/', SurveyCreateView.as_view()),
    path('surveys/update/<int:pk>', SurveyUpdateView.as_view()),
    path('votefacts/getAll', VoteFactListView.as_view()),

    path('questions/delete/<int:pk>', QuestionDeleteView.as_view()),
    path('questions/create/', QuestionCreateView.as_view()),
    path('questions/update/<int:pk>', QuestionUpdateView.as_view()),

    path('answers/delete/<int:pk>', AnswerDeleteView.as_view()),
    path('answers/create/', AnswerCreateView.as_view()),
    path('answers/update/<int:pk>', AnswerUpdateView.as_view())

]
