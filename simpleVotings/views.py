from rest_framework import status, generics
from rest_framework.exceptions import PermissionDenied

from .models import *
from .serializers import *


class SurveyUpdateView(generics.UpdateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveyUpdateSerializer


class SurveyCreateView(generics.CreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class SurveyDeleteView(generics.DestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerUpdateView(generics.UpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDeleteView(generics.DestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerListView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()

        params = self.request.query_params

        user_id = params.get('user_id', None)

        if user_id:
            queryset = queryset.filter(author_id=user_id)

        return queryset


class AnswerListView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()

        params = self.request.query_params

        user_id = params.get('user_id', None)

        if user_id:
            queryset = queryset.filter(author_id=user_id)

        return queryset


class VoteFactListView(generics.ListAPIView):
    serializer_class = VoteFactSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()

        params = self.request.query_params

        user_id = params.get('user_id', None)

        if user_id:
            queryset = queryset.filter(votefact__author_id=user_id)

        return queryset


class VoteFactCreateView(generics.CreateAPIView):
    serializer_class = VoteFactSerializer
    queryset = VoteFact.objects.all()


class VoteFactUpdateView(generics.UpdateAPIView):
    serializer_class = VoteFactSerializer
    queryset = VoteFact.objects.all()


class VoteFactDeleteView(generics.DestroyAPIView):
    serializer_class = VoteFactSerializer
    queryset = VoteFact.objects.all()
