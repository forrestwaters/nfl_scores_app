from django.conf.urls import url
from live_scores import views

urlpatterns = [
    # tells /live_scores to
    url(r'^$', views.scores),
]
