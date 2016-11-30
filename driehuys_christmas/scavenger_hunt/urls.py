from django.conf.urls import include, url

from scavenger_hunt import views


urlpatterns = [
    url(r'^', views.HuntListView.as_view(), name='hunt-list'),
]
