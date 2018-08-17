from django.contrib     import admin
from .models            import EventRegistration, Event, Event_Type, Event_Subtype, Age_Group,Level,Venue, Room, Period, Host, Weekday


class AgeGroupAdmin(admin.ModelAdmin):  
    list_display    = ['age_group']
    ordering        = ('age_group',)


class RoomAdmin(admin.ModelAdmin):  
    list_display    = ['venue', 'room']
    ordering        = ('venue','room')

class HostAdmin(admin.ModelAdmin):  
    list_display    = ['firstname', 'lastname', 'image', 'resume']
    ordering        = ('firstname', 'lastname')



admin.site.register(EventRegistration)
admin.site.register(Event)
admin.site.register(Event_Type)
admin.site.register(Event_Subtype)
admin.site.register(Age_Group, AgeGroupAdmin)
admin.site.register(Level)
admin.site.register(Venue)
admin.site.register(Room, RoomAdmin)
admin.site.register(Period)
admin.site.register(Host, HostAdmin)
admin.site.register(Weekday)