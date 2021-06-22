from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    survey_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    end_date = models.DateTimeField()
    survey_description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.survey_name


class Question(models.Model):
    QUESTION_TYPES = [
        ('1', 'one answer'),
        ('2', 'many answers'),
        ('3', 'custom answer')
    ]
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(choices=QUESTION_TYPES, max_length=200, default='1')

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=254)


class VoteFact(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)

