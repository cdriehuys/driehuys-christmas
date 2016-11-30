from django.conf.urls import url
from django.views.generic.base import TemplateView


index_view = TemplateView.as_view(template_name='core/index.html')


app_name = 'core'


urlpatterns = [
    url(r'^$', index_view, name='index'),
]
