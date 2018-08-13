from django.db                      import models
from django.contrib.auth.models     import User
from accounts.models                import Profile

# Comments :
# <!> Make the distinction between "Event" and "OneTimeEvent" :
# <!> All entries are events, some of them are "activities", other "TrainingCourse" and others "OneTimeEvent"
# <!> The app is named "activities", it should have been named "Events".EVENT



class Event_Type(models.Model):
    
    ACTIVITY        = 'ACTIVITY'
    TRAININGCOURSE  = 'TRAININGCOURSE'
    ONETIMEEVENT    = 'EVENT'
    
    TYPE = (
        (ACTIVITY,         'ACTIVITY'       ),
        (TRAININGCOURSE,   'TRAININGCOURSE' ),
        (ONETIMEEVENT,     'EVENT'          ),
    )
    
    event_type      = models.CharField(max_length=50, choices=TYPE)
    title           = models.CharField(max_length=50, null=True)
    description     = models.TextField(null=True)
    image           = models.ImageField(upload_to="images/event_type", blank=True, null=True)
    
    def __str__(self):
        return self.event_type



class Event_Subtype(models.Model):
    
    event_subtype   = models.CharField(max_length=100, null=False)
    description     = models.TextField(null=True)
    image           = models.ImageField(upload_to="images/event_subtype", blank=True, null=True)
    
    def __str__(self):
        return self.event_subtype


        
class Weekday(models.Model):
    
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
    
    day             = models.CharField(max_length=10, choices=WEEKDAY_CHOICES)
    
    def __str__(self):
        return self.day



class Period(models.Model):
    
    period          = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return self.period



class Host(models.Model):
    
    firstname   = models.CharField(max_length=100, null=False)
    lastname    = models.CharField(max_length=100, null=False)
    image       = models.ImageField(upload_to="images/hosts/", default = "noimage.jpg")
    resume      = models.TextField(null=True)
    
    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)



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
    
    venue           = models.ForeignKey(Venue, related_name="Room", on_delete=models.SET_DEFAULT, default= 1, null=False)
    room            = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return '%s - Salle %s' % (self.venue, self.room)



class Event(models.Model):
    
    event_type        = models.ForeignKey(Event_Type, related_name="Event", on_delete=models.SET_DEFAULT, default= 1, null=False)
    event_subtype     = models.ForeignKey(Event_Subtype, related_name="Event", on_delete=models.SET_DEFAULT, default= 1, null=False)
    name              = models.CharField(max_length=100)
    period            = models.ForeignKey(Period, related_name="Event", on_delete=models.SET_DEFAULT, default= 1, null=False)
    host              = models.ForeignKey(Host, related_name="Event", on_delete=models.SET_DEFAULT, default= 1, null=True)
    description       = models.TextField()
    image             = models.ImageField(upload_to="images/events/", default = "noimage.jpg")
    day               = models.ForeignKey(Weekday, related_name="Event", on_delete=models.SET_DEFAULT, default= 1)
    time_start        = models.TimeField(null=True)
    time_end          = models.TimeField(null=True)
    rate              = models.DecimalField(max_digits=6, decimal_places=2)
    age_group         = models.ForeignKey(Age_Group, related_name="Event", on_delete=models.SET_DEFAULT, default= 1, null=False)
    level             = models.ForeignKey(Level, related_name="Event", on_delete=models.SET_DEFAULT, default= 1, null=False)
    number_max        = models.PositiveSmallIntegerField(null=False)
    number_available  = models.PositiveSmallIntegerField(null=True)
    room              = models.ForeignKey(Room, related_name="Event", on_delete=models.SET_DEFAULT, default= 1, null=False)
    
    def __str__(self):
        return self.name
        
        
        
class EventRegistration(models.Model):
    
    participant         = models.ForeignKey(User, related_name="RegistrationList", on_delete=models.SET_DEFAULT, default= 1, null=False)
    event               = models.ForeignKey(Event, related_name="RegistrationList", on_delete=models.SET_DEFAULT, default= 1, null=False)
    
    class Meta:
        unique_together = ["participant", "event"]
    
    def __str__(self):
        return 'Event Registration N° %s' % (self.id)
        
        
# ----------------------------------------------------------------------

    # It's possible to define a function to automatically fill a field : 
    # @property
    # def banana_1(self):
    #     return "This is the value"
    
    # @property
    # def banana_2(self):
    #     return "This is the value"