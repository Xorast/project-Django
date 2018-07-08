from django.contrib     import admin
from .models            import Event, Event_Type, Event_Subtype,Age_Group,Level,Venue, Room


admin.site.register(Event)
admin.site.register(Event_Type)
admin.site.register(Event_Subtype)
admin.site.register(Age_Group)
admin.site.register(Level)
admin.site.register(Venue)
admin.site.register(Room)