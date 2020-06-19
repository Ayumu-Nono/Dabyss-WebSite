from django.urls import path
from .views import BlogListView

app_name = 'articles'
urlpatterns = [
    path('blog/', BlogListView.as_view(), name="bloglist"),
]