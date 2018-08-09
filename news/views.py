from django.shortcuts               import render, get_object_or_404
from .models                        import News


def get_news_list(request):
    news    = News.objects.all
    return render(request, "news/news_list.html", {"news" : news})
