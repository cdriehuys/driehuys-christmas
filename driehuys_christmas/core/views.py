from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    """
    Display the index page.

    If the requesting user is already authenticated, they should be
    redirected to the scavenger hunt list page.
    """
    authenticated_redirect_url = reverse_lazy('scavenger_hunt:hunt-list')
    template_name = 'core/index.html'

    def get(self, request, **kwargs):
        """
        Display the index view.
        """
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.authenticated_redirect_url)

        return super(IndexView, self).get(request, **kwargs)
