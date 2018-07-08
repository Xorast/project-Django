from django.db import models



class Event_Type(models.Model):
    
    event_type      = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.event_type

class Event_Subtype(models.Model):
    
    event_subtype   = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.event_subtype

class Age_Group(models.Model):
    
    age_group       = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.age_group

class Level(models.Model):
    
    level           = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.level

class Venue(models.Model):
    
    name            = models.CharField(max_length=100, null=False)
    street_nb       = models.CharField(max_length=20, null=False)
    street_name     = models.CharField(max_length=200, null=False)
    city            = models.CharField(max_length=100, null=False)
    postcode        = models.PositiveSmallIntegerField(null=False)
    url_map         = models.URLField(max_length=200)
    
    
    def __str__(self):
        return self.name

class Room(models.Model):
    
    venue           = models.ForeignKey(Venue, related_name="room", on_delete=models.SET_DEFAULT, default= 1, null=False)
    room            = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return '%s - Salle %s' % (self.venue, self.room)



class Event(models.Model):
    
    MONDAY      = 'MONDAY'
    TUESDAY     = 'TUESDAY'
    WEDNESDAY   = 'WEDNESDAY'
    THURSDAY    = 'THURSDAY'
    FRIDAY      = 'FRIDAY'
    SATURDAY    = 'SATURDAY'
    SUNDAY      = 'SUNDAY'
    
    WEEKDAY_CHOICES = (
        (MONDAY,    'MONDAY'    ),
        (TUESDAY,   'TUESDAY'   ),
        (WEDNESDAY, 'WEDNESDAY' ),
        (THURSDAY,  'THURSDAY'  ),
        (FRIDAY,    'FRIDAY'    ),
        (SATURDAY,  'SATURDAY'  ),
        (SUNDAY,    'SUNDAY'    ),
    )
    
    event_type      = models.ForeignKey(Event_Type, related_name="event", on_delete=models.SET_DEFAULT, default= 1, null=False)
    event_subtype   = models.ForeignKey(Event_Subtype, related_name="event", on_delete=models.SET_DEFAULT, default= 1, null=False)
    name            = models.CharField(max_length=100)
    description     = models.TextField()
    image           = models.ImageField(upload_to="images", default = "noimage.jpg")
    day             = models.CharField(max_length=10, choices=WEEKDAY_CHOICES)
    time_start      = models.TimeField(null=True)
    time_end        = models.TimeField(null=True)
    rate            = models.DecimalField(max_digits=6, decimal_places=2)
    age_group       = models.ForeignKey(Age_Group, related_name="event", on_delete=models.SET_DEFAULT, default= 1, null=False)
    level           = models.ForeignKey(Level, related_name="event", on_delete=models.SET_DEFAULT, default= 1, null=False)
    number_max      = models.PositiveSmallIntegerField(null=False)
    room            = models.ForeignKey(Room, related_name="event", on_delete=models.SET_DEFAULT, default= 1, null=False)
    
    def __str__(self):
        return self.name





















# class Venue(models.Model):
    
#     default         = "Te be determined"
    
#     venue   = models.CharField(max_length=200, default = default, null=False)
    
#     def __str__(self):
#         return self.type_category
        
# class Leader(models.Model):
    
#     default         = "Te be determined"
    
#     leader   = models.CharField(max_length=200, default = default, null=False)
    
#     def __str__(self):
#         return self.type_category

# class Level(models.Model):
    
#     default         = "Te be determined"
    
#     level   = models.CharField(max_length=200, default = default, null=False)
    
#     def __str__(self):
#         return self.type_category



# class Activity(models.Model):
    
#     default_leader      = 'To be determined'
#     default_venue       = 'To be determined'
#     default_age_range   = 'To be determined'
#     default_level       = 'To be determined'
    
#     name            = models.CharField(max_length=100)
#     type_category   = models.ForeignKey(Type_category, related_name='activity', on_delete=models.SET(get_deleted), null=True)
#     # age_range       = models.ForeignKey(table_age_range, related_name="activity", on_delete=models.SET(default_age_range), null=False)
#     level           = models.ForeignKey(Level, related_name="activity", on_delete=models.SET(get_deleted), null=False)
#     description     = models.TextField()
#     # day             = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
#     time_start      = models.TimeField(auto_now=False, auto_now_add=False)
#     time_end        = models.TimeField(auto_now=False, auto_now_add=False)
#     venue           = models.ForeignKey(Venue,  related_name='activity', on_delete=models.SET(get_deleted), null=False)
#     leader          = models.ForeignKey(Leader, related_name='activity', on_delete=models.SET(get_deleted), null=False)
#     # image           = models.ImageField(upload_to="images", blank=True, null=True)
#     rate            = models.DecimalField(max_digits=6, decimal_places=2)
    
#     def __str__(self):
#         return self.name
