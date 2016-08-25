from django import forms
from django.forms import formset_factory

from .models import Question, Choice

# Forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)

    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = True

ChoiceFormSet = formset_factory(ChoiceForm, extra=3)