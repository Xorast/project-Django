from django.shortcuts               import render, redirect, get_object_or_404, HttpResponse
from .models                        import Activity_Animation_Type, Activity_Animation, Activity_Animation_Slot, Elements_Type, Host
from django.contrib.auth.decorators import login_required
# from .models                        import EventRegistration






def get_list_of_animation_types(request):
    
    return render(request, "activities/list_of_animation_types.html")



def research(request):
    
    activities = Activity_Animation_Slot.objects.all().order_by('animation__animation_type','animation')
    
    return render(request, "activities/research_activities.html", {'activities':activities})



def get_list_of_animations(request, animation_type):
    
    animations_type = get_object_or_404(Activity_Animation_Type, animation_type=animation_type)
    animations      = Activity_Animation.objects.filter(animation_type=animations_type.id).order_by('name')
    
    return render(request, "activities/list_of_animations.html", {'animations_type':animations_type,'animations':animations})



def get_animation_details(request, animation_type, animation, animation_id):

    animation       = get_object_or_404(Activity_Animation, id=animation_id)
    slots           = Activity_Animation_Slot.objects.filter(animation=animation).order_by('age_group__age_min','age_group__age_max','day_id','time_start')
    
    hosts = []
    # for slot in slots:
    #   host = Host.objects.filter(Slot = slot.id)
    #   for h in host:
    #       hosts.append(h)  
    [[hosts.append(h) for h in Host.objects.filter(Slot = slot.id)] for slot in slots]
    hosts = list(set(hosts))
    
    unmentionned_rate_text = "Si le tarif n'est pas indiqué dans les notes, contacter la MJC."
    two_rates_no_info_on_second_rate = "Contacter la MJC pour connaitre les conditions du deuxième tarif."
    
    return render(request, "activities/animation_details.html", {'animation':animation,'slots':slots, 'hosts':hosts, 'unmentionned_rate_text':unmentionned_rate_text, 'two_rates_no_info_on_second_rate':two_rates_no_info_on_second_rate})




# To be deleted
# def get_type_subtypes(request, event_type):
    
#     event_type      = get_object_or_404(Event_Type, event_type=event_type)
#     event_subtypes  = Event_Subtype.objects.filter(Event__event_type = event_type.id).distinct().order_by('event_subtype')
    
#     return render(request, "activities/events_list_of_type_subtypes.html", {"event_type" : event_type, "event_subtypes" : event_subtypes})
    

# To be deleted 
# def get_subtype_list(request, event_type, event_subtype):
    
#     event_type      = get_object_or_404(Event_Type, event_type=event_type)
#     event_subtype   = get_object_or_404(Event_Subtype, event_subtype=event_subtype)
#     events          = Event.objects.filter(event_type__event_type=event_type, event_subtype__event_subtype=event_subtype).order_by('name')
    
#     return render(request, "activities/events_list_by_type_subtypes.html", {"event_type" : event_type, "event_subtype":event_subtype, "events": events})


# To be deleted
# def get_event_details(request, event_type, event_subtype, event_id):
    
#     event           = get_object_or_404(Event, pk=event_id)
    
#     return render(request, "activities/event_details.html", {"event": event})


# To be deleted
# @login_required
# def register_to_event(request, event_type, event_subtype, event_id):
    
#     event   = get_object_or_404(Event, pk=event_id)
    
#     if event.number_available > 0 :
    
#         check   = EventRegistration.objects.filter(participant=request.user,event=event).count()
        
#         if check == 0:
            
#             return render(request, "activities/event_registration.html", {"event": event})
            
#         else:
            
#             error = "You are already registered to this event. If you want to register someone else, please login under with his/her session."
#             return render(request, "activities/event_registration_request_failed.html", {"error":error})
            
#     else:
        
#         error = "There are no place available."
#         return render(request, "activities/event_registration_request_failed.html", {"error":error})