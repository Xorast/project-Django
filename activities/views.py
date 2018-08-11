from django.shortcuts               import render, redirect, get_object_or_404, HttpResponse
from .models                        import Event, Event_Type, Event_Subtype, EventRegistration
from django.contrib.auth.decorators import login_required



def get_home_page(request):
    return render(request, "activities/index.html")


    
def get_type_subtypes(request, event_type):
    
    event_type      = get_object_or_404(Event_Type, event_type=event_type)
    event_subtypes  = Event_Subtype.objects.filter(Event__event_type = event_type.id).distinct()
    
    return render(request, "activities/events_list_of_type_subtypes.html", {"event_type" : event_type, "event_subtypes" : event_subtypes})


    
def get_subtype_list(request, event_type, event_subtype):
    
    event_type      = get_object_or_404(Event_Type, event_type=event_type)
    event_subtype   = get_object_or_404(Event_Subtype, event_subtype=event_subtype)
    events          = Event.objects.filter(event_type__event_type=event_type, event_subtype__event_subtype=event_subtype)
    
    return render(request, "activities/events_list_by_type_subtypes.html", {"event_type" : event_type, "event_subtype":event_subtype, "events": events})



def get_event_details(request, event_type, event_subtype, event_id):
    
    event           = get_object_or_404(Event, pk=event_id)
    
    return render(request, "activities/event_details.html", {"event": event})



@login_required
def register_to_event(request, event_type, event_subtype, event_id):
    
    event           = get_object_or_404(Event, pk=event_id)

    return render(request, "activities/event_registration.html", {"event": event})



@login_required
def register_confirm_request(request, event_type, event_subtype, event_id):
    
    event   = get_object_or_404(Event, pk=event_id)
    ER      = EventRegistration(participant=request.user,event=event)
    
    error   = ""
    
    if event.number_available > 0 :
    
        try:
            # Constraint on the model : user / event combination must be unique
            # If the user is already registered : will throw an error
            ER.save()
    
            event.number_available += -1
            event.save()
            
        except:
            error = "E01"
            return render(request, "activities/event_registration_request_failed.html", {"error":error})
    
    else:
        error = "E02"
        return render(request, "activities/event_registration_request_failed.html", {"error":error})
        
    return render(request, "activities/event_registration_request_successful.html")