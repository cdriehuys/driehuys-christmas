from django.conf import settings
from django.db import models


class ScavengerHunt(models.Model):
    """
    Model representing an entire scavenger hunt.
    """
    completed = models.BooleanField(default=False)
    final_text = models.TextField(help_text='This text will be displayed after all puzzles in the hunt are completed.')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self) -> str:
        """
        Return a string describing this scavenger hunt.
        """
        return "Scavenger hunt for {user}".format(user=self.user.username)
