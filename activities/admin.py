from django.contrib     import admin
from .models            import Elements_Type, Animation_Type, Animation, Weekday, Period, Host, Age_Class, Age_Group, Level, City, Venue, Room, ActivitySlot


class RoomAdmin(admin.ModelAdmin):  
    list_display    = ['venue', 'room']
    ordering        = ('venue','room')

class HostAdmin(admin.ModelAdmin):  
    list_display    = ['firstname', 'lastname', 'image', 'resume']
    ordering        = ('firstname', 'lastname')



admin.site.register(Elements_Type)
admin.site.register(Animation_Type)
admin.site.register(Animation)
admin.site.register(Weekday)
admin.site.register(Period)
admin.site.register(Host, HostAdmin)
admin.site.register(Age_Class)
admin.site.register(Age_Group)
admin.site.register(Level)
admin.site.register(City)
admin.site.register(Venue)
admin.site.register(Room, RoomAdmin)
admin.site.register(ActivitySlot)