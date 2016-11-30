from django.conf.urls import include, url

from scavenger_hunt import views


app_name = 'scavenger_hunt'


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.HuntDetailView.as_view(), name='hunt-detail'),
    url(r'^', views.HuntListView.as_view(), name='hunt-list'),
]
