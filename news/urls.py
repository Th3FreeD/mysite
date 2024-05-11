from django.urls import include, path
from django.views.generic import ListView, DetailView
from news.models import Articles

urlpatterns = [
    #Отображение всех статей, -date позволяет выводить сначала новые статьи, а потом старые. [:20] - срез до 20 постов (ограничение)
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name="news/posts.html")),
    #Отображение страниц для каждой статьи, ее описание
    path('<int:pk>/', DetailView.as_view(model = Articles, template_name = "news/post.html"))
]
