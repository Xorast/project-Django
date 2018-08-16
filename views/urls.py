from django.conf.urls.static    import static
from django.views.static        import serve
from django.conf                import settings
from django.urls                import path
from .views                     import get_home_page, get_admin_panel, get_about_page


# For the featuring of subtypes : instead of 3 URL : make only one with a variable. Like djangoblog.

urlpatterns = [
    path('', get_home_page, name='home'),
    path('admin_panel', get_admin_panel, name='admin_panel'),
    path('about', get_about_page, name='about'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
]