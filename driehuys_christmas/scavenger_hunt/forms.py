from django import forms
from django.core.exceptions import ValidationError


class PuzzleAnswerForm(forms.Form):
    """
    Form for submitting puzzle answers.
    """
    answer = forms.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with an associated scavenger hunt.
        """
        self.puzzle = kwargs.pop('puzzle')

        super(PuzzleAnswerForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        Ensure that the provided answer is correct.
        """
        super(PuzzleAnswerForm, self).clean()

        answer = self.cleaned_data['answer']

        if not self.puzzle.is_valid_answer(answer):
            raise ValidationError("Sorry, your answer is incorrect.")
