from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property


class Puzzle(models.Model):
    """
    Model representing a single puzzle in a scavenger hunt.
    """
    answer = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    hunt = models.ForeignKey('scavenger_hunt.ScavengerHunt')
    order = models.PositiveIntegerField(default=0)
    text = models.TextField()
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        """
        Return the puzzle's title.
        """
        return self.title

    def get_absolute_url(self):
        """
        Get the url of the puzzle's detail view.
        """
        return reverse('scavenger_hunt:puzzle-detail', kwargs={'hunt_pk': self.hunt.pk, 'pk': self.pk})

    def is_valid_answer(self, answer):
        """
        Determine if the provided answer is correct.
        """
        return answer == self.answer


class ScavengerHunt(models.Model):
    """
    Model representing an entire scavenger hunt.
    """
    completed = models.BooleanField(default=False)
    final_text = models.TextField(help_text='This text will be displayed after all puzzles in the hunt are completed.')
    time_created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ('time_created',)

    def __str__(self) -> str:
        """
        Return the hunt's title.
        """
        return self.title

    @cached_property
    def decimal_completion(self) -> float:
        """
        Get the hunt's progress as a float between 0 and 1.

        Returns:
            The number of completed puzzles in the hunt divided by the
            total number of puzzles in the hunt.
        """
        puzzles = Puzzle.objects.filter(hunt=self)
        completed = puzzles.filter(completed=True)

        return completed.count() / puzzles.count()

    def get_absolute_url(self) -> str:
        """
        Get the URL of the hunt's detail view.
        """
        return reverse('scavenger_hunt:hunt-detail', kwargs={'pk': self.pk})

    def percent_completion(self) -> float:
        """
        Get the hunt's progress as a float between 0 and 100.

        Returns:
            ``decimal_completion`` multiplied by 100.
        """
        return self.decimal_completion * 100
