from django import forms

from .models import Question

# Forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)