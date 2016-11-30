from django.views import generic

from scavenger_hunt import models


class HuntDetailView(generic.DetailView):
    """
    View for displaying a scavenger hunt's details.
    """
    model = models.ScavengerHunt
    template_name = 'scavenger_hunt/hunt_detail.html'


class HuntListView(generic.base.TemplateView):
    """
    View for listing scavenger hunts.
    """
    template_name = 'scavenger_hunt/hunt_list.html'

    def get_context_data(self, **kwargs):
        """
        Get the context for the view.
        """
        context = super(HuntListView, self).get_context_data(**kwargs)

        context['hunts'] = self.request.user.scavengerhunt_set.all()

        return context
