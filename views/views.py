from django.shortcuts       import render, redirect, get_object_or_404
from activities.models      import Event_Type
from news.models            import News



def get_home_page(request):
    
    last_news    = News.objects.order_by('-published_date')[:2]
    activities   = get_object_or_404(Event_Type, event_type="ACTIVITY")
    courses      = get_object_or_404(Event_Type, event_type="TRAININGCOURSE")
    events       = get_object_or_404(Event_Type, event_type="EVENT")
    
    return render(request, "views/index.html", {'last_news': last_news, 'activities': activities, 'courses': courses, 'events': events})


def get_admin_panel(request):
    return redirect("/admin")
    
    
    
def get_about_page(request):
    return render(request, "views/about.html")