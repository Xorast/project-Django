from django.conf.urls.static    import static
from django.views.static        import serve
from django.conf                import settings
from django.urls                import path
from .views                     import get_list_of_all_events, get_event_details, get_event_file



urlpatterns = [
    path('list-of-all-events', get_list_of_all_events, name='list-of-all-events'),
    path('<event_id>', get_event_details, name='event_details'),
    path('<event_id>/file', get_event_file, name='event_file'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
]