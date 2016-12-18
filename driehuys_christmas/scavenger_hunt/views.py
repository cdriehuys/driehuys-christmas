from django.http import HttpResponseRedirect
from django.views import generic

from scavenger_hunt import models


class HuntDetailView(generic.DetailView):
    """
    View for displaying a scavenger hunt's details.
    """
    model = models.ScavengerHunt
    template_name = 'scavenger_hunt/hunt_detail.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data to be passed to the template.
        """
        context = super(HuntDetailView, self).get_context_data(**kwargs)

        context['puzzles'] = self.object.puzzle_set.all()

        return context


class HuntListView(generic.ListView):
    """
    View for listing scavenger hunts.
    """
    context_object_name = 'hunts'
    model = models.ScavengerHunt
    template_name = 'scavenger_hunt/hunt_list.html'

    def get(self, request, *args, **kwargs):
        """
        Redirect if there is only one hunt.
        """
        objects = self.get_queryset()
        if objects.count() == 1:
            obj = objects.get()
            url = obj.get_absolute_url()

            return HttpResponseRedirect(url)

        return super(HuntListView, self).get(request, *args, **kwargs)


class PuzzleDetailView(generic.DetailView):
    """
    View for displaying a puzzle's details.
    """
    model = models.Puzzle
    template_name = 'scavenger_hunt/puzzle_detail.html'
