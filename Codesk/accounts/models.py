from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    coursecode = models.CharField(default='XXXXXX', max_length=8)
    title = models.TextField()
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class QuestionComment(models.Model):
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    belongs_to = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Answer(models.Model):
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    votes = models.IntegerField(default='0')
    belongs_to = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class AnswerComment(models.Model):
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    votes = models.IntegerField(default='0')
    belongs_to = models.ForeignKey(Answer, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Notes(models.Model):
    coursecode = models.CharField(max_length=8)
    title = models.TextField()
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    votes = models.IntegerField(default='0')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
