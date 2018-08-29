from django.conf.urls.static    import static
from django.views.static        import serve
from django.conf                import settings
from django.urls                import path
from .views                     import get_list_of_all_events, get_event_details



urlpatterns = [
    path('list-of-all-events', get_list_of_all_events, name='list-of-all-events'),
    path('<event_id>', get_event_details, name='event_details'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
    # path('list-of-animation-types', get_list_of_animation_types, name="w_list_of_animations_types"),
    # path('<animation_type>', get_list_of_animations, name="w_list_of_animations"),
    # path('<animation_type>/<animation>/<animation_id>', get_animation_details, name="w_animation_details"),
    # path('<event_type>/<event_subtype>/<event_id>/registration', register_to_event, name='register_to_event'),
]