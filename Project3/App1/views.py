from django.views.generic import ListView, TemplateView
from .models import Post


# Create your views here.
class PostViews(ListView):
    model = Post
    template_name = 'HomePage.html'


class NewsViews(TemplateView):
    template_name = 'News.html'
