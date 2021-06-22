from rest_framework import serializers
from .models import *


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


class SurveyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('survey_name', 'end_date', 'survey_description', 'is_active',)


class VoteFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteFact
        fields = '__all__'
