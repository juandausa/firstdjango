from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import datetime
from django.utils import timezone

# Models


@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_votes(self):
        votes = 0
        for _choice in self.choice_set.all():
            votes += _choice.votes
        return votes

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, blank=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
