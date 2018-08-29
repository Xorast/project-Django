from django.shortcuts       import render, redirect, get_object_or_404, HttpResponse
from .models                import Event_Family, Event





def get_list_of_all_events(request):
    
    events = Event.objects.order_by('date_first_day')
    
    return render(request, "events/list_of_all_events.html", {'events':events})
    
    
    
def get_event_details(request, event_id):
    
    event = get_object_or_404(Event, id=event_id)
    
    return render(request, "events/event_details.html", {'event':event})