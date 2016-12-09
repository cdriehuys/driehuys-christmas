from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


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

    def get_absolute_url(self) -> str:
        """
        Get the URL of the hunt's detail view.
        """
        return reverse('scavenger_hunt:hunt-detail', kwargs={'pk': self.pk})
