from django.conf.urls.static    import static
from django.views.static        import serve
from django.conf                import settings
from django.urls                import path
from .views                     import get_home_page, get_about_page, get_venue, get_venues_list, get_host, get_admin_panel, get_rate_and_registration_activities_page, get_rate_and_registration_workshop_page    


# For the featuring of subtypes : instead of 3 URL : make only one with a variable. Like djangoblog.

urlpatterns = [
    path('', get_home_page, name='home'),
    path('about', get_about_page, name='about'),
    path('rate_and_registration_activities', get_rate_and_registration_activities_page, name='rate_and_registration_activities'),
    path('rate_and_registration_workshops', get_rate_and_registration_workshop_page, name='rate_and_registration_workshops'),
    path('venue/<name_venue>', get_venue, name='venue'),
    path('venues', get_venues_list, name='venues_list'),
    path('host/<id>', get_host, name='host'),
    path('admin_panel', get_admin_panel, name='admin_panel'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
]