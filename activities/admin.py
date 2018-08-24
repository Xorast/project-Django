from django.contrib     import admin
from .models            import EventRegistration, Event, Event_Type, Animation_Type, Animation, Age_Class, Age_Group, Level, City, Venue, Room, Period, Host, Weekday


class RoomAdmin(admin.ModelAdmin):  
    list_display    = ['venue', 'room']
    ordering        = ('venue','room')

class HostAdmin(admin.ModelAdmin):  
    list_display    = ['firstname', 'lastname', 'image', 'resume']
    ordering        = ('firstname', 'lastname')



admin.site.register(EventRegistration)
admin.site.register(Event)
admin.site.register(Event_Type)
admin.site.register(Animation)
admin.site.register(Animation_Type)
admin.site.register(Age_Class)
admin.site.register(Age_Group)
admin.site.register(Level)
admin.site.register(City)
admin.site.register(Venue)
admin.site.register(Room, RoomAdmin)
admin.site.register(Period)
admin.site.register(Host, HostAdmin)
admin.site.register(Weekday)