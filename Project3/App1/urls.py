from django.urls import path
from .views import PostViews, NewsViews

urlpatterns = [
    path('', PostViews.as_view(), name='Post'),
    path('News/', NewsViews.as_view(), name='News'),
]
