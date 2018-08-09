from django.shortcuts               import render, get_object_or_404, HttpResponse
from .models                        import Event, Event_Type, Event_Subtype
from django.contrib.auth.decorators import login_required



def get_home_page(request):
    return render(request, "activities/index.html")


    
def get_type_subtypes(request, event_type):
    
    event_type      = get_object_or_404(Event_Type, event_type=event_type)
    event_subtypes  = Event_Subtype.objects.filter(Event__event_type = event_type.id).distinct()
    
    return render(request, "activities/subtype_main.html", {"event_type" : event_type, "event_subtypes" : event_subtypes})


    
def get_subtype_list(request, event_type, event_subtype):
    
    event_type      = get_object_or_404(Event_Type, event_type=event_type)
    event_subtype   = get_object_or_404(Event_Subtype, event_subtype=event_subtype)
    events          = Event.objects.filter(event_type__event_type=event_type, event_subtype__event_subtype=event_subtype)
    
    return render(request, "activities/events_list_by_type_subtypes.html", {"event_type" : event_type, "event_subtype":event_subtype, "events": events})



def get_event_details(request, event_type, event_subtype, event_id):
    
    event           = get_object_or_404(Event, pk=event_id)
    
    return render(request, "activities/event_details.html", {"event": event})



@login_required
def get_confirmation(request):
    return HttpResponse('=)')