from activities.models      import Activity_Animation_Type, Elements_Type
from workshops.models       import Workshop_Animation_Type







def get_list_of_animation_types_activities(request):
    
   animations_types_activities = Activity_Animation_Type.objects.all().order_by('animation_type')

   return {'animations_types_activities':animations_types_activities}



def get_list_of_animation_types_workshops(request):
    
   animations_types_workshops = Workshop_Animation_Type.objects.all().order_by('animation_type')

   return {'animations_types_workshops':animations_types_workshops}
   
   
   
def get_elements_types(request):
    
    
    try:
        activity = Elements_Type.objects.get(element_type__exact="ACTIVITY")
        workshop = Elements_Type.objects.get(element_type__exact="WORKSHOP")
        event    = Elements_Type.objects.get(element_type__exact="EVENT")
    except:
        activity = "Your admin need to fix that! =)"
        workshop = "Your admin need to fix that! =)"
        event    = "Your admin need to fix that! =)"
    
    return {'activity':activity, 'workshop':workshop, 'event':event}
   
   
   
   
   
   
   
   
   
   
# If context processor still required, do it by objects.filter instead of get_object_or_404

# def get_list_of_type_subtypes(request):
    
#     event_type_ACTIVITY       = get_object_or_404(Event_Type, event_type='ACTIVITY')
#     event_subtypes_ACTIVITY   = Event_Subtype.objects.filter(Event__event_type = event_type_ACTIVITY.id).distinct().order_by('event_subtype')
    
#     event_type_COURSE         = get_object_or_404(Event_Type, event_type='TRAININGCOURSE')
#     event_subtypes_COURSE     = Event_Subtype.objects.filter(Event__event_type = event_type_COURSE.id).distinct().order_by('event_subtype')
    
#     event_type_EVENT          = get_object_or_404(Event_Type, event_type='EVENT')
#     event_subtypes_EVENT      = Event_Subtype.objects.filter(Event__event_type = event_type_EVENT.id).distinct().order_by('event_subtype')
    
#     return { 'event_subtypes_ACTIVITY'  : event_subtypes_ACTIVITY, 
#              'event_subtypes_COURSE'    : event_subtypes_COURSE, 
#              'event_subtypes_EVENT'     : event_subtypes_EVENT }
    
    