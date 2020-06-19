from django.urls import path
from .views import BlogListView, GameListView

app_name = 'articles'
urlpatterns = [
    path('blog/', BlogListView.as_view(), name="bloglist"),
    path('games/', GameListView.as_view(), name="gamelist"),
]