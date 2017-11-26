from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
        def get(self, request, **kwargs):
                    return render(request, 'bootstrap/index.html', context=None)
