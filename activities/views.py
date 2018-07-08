from django.shortcuts   import render
from .models            import Event



def get_home_page(request):
    events = Event.objects.all()
    return render(request, "activities/index.html", {"events" : events})