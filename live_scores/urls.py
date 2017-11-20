from django.conf.urls import url
from live_scores import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
