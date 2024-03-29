from django.shortcuts import render
from django.views.generic import ListView
from .models import Content
from django.contrib.auth.decorators import login_required


# Create your views here.

#@login_required
class ContentView(ListView):
    """Retrieves news content data from db"""
    template_name = 'index.html'
    model = Content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contents'] = Content.objects.filter().order_by('-pub_date')[:10]
        return context

def about_us(request):
    """Processes the about page"""
    template_name = 'about.html'
    return render(request, template_name)
