from django.conf.urls.static    import static
from django.views.static        import serve
from django.conf                import settings
from django.urls                import path
from .views                     import get_news_list


urlpatterns = [
    path('', get_news_list, name='news_list'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
]