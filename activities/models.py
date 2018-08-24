from django.db                      import models
from django.contrib.auth.models     import User
from accounts.models                import Profile
from django.contrib.postgres.fields import ArrayField

# Comments :
# <!> Make the distinction between "Event" and "OneTimeEvent" :
# <!> All entries are events / element, some of them are "activities", other "TrainingCourse" and others "OneTimeEvent"
# <!> The app is named "activities", it should have been named "Element"



class Event_Type(models.Model):
    
    ACTIVITY        = 'ACTIVITY'
    TRAININGCOURSE  = 'TRAININGCOURSE'
    ONETIMEEVENT    = 'EVENT'
    
    TYPE = (
        (ACTIVITY,         'ACTIVITY'       ),
        (TRAININGCOURSE,   'TRAININGCOURSE' ),
        (ONETIMEEVENT,     'EVENT'          ),
    )
    
    event_type      = models.CharField("Type d'élément", max_length=50, choices=TYPE)
    title           = models.CharField("Label", max_length=50, null=True)
    description     = models.TextField("Description", null=True)
    image           = models.ImageField("Image", upload_to="images/event_type", blank=True, null=True)
    
    def __str__(self):
        return self.event_type

    class Meta:
            verbose_name = "Eléments - Type"
            verbose_name_plural = "Eléments - Types"
    
    

class Animation_Type(models.Model):
    
    animation_type  = models.CharField("Type d'animation", max_length=100, null=False)
    description     = models.TextField("Description", null=True)
    image           = models.ImageField("Image", upload_to="images/animation_type", blank=True, null=True)
    
    def __str__(self):
        return self.animation_type

    class Meta:
            verbose_name = "Animation - Type"
            verbose_name_plural = "Animations - Types"
            


class Animation(models.Model):
    
    name              = models.CharField("Nom", max_length=100)
    animation_type    = models.ForeignKey(Animation_Type, related_name="Animation", on_delete=models.SET_NULL, null=True)
    image             = models.ImageField("Image", upload_to="images/animation/", default = "noimage.jpg")
    description       = models.TextField()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Animation'
        verbose_name_plural = 'Animations'
        
        
        
class Weekday(models.Model):
    
    LUNDI      = 'Lundi'
    MARDI      = 'Mardi'
    MERCREDI   = 'Mercredi'
    JEUDI      = 'Jeudi'
    VENDREDI   = 'Vendredi'
    SAMEDI     = 'Samedi'
    DIMANCHE   = 'Dimanche'
    
    WEEKDAY_CHOICES = (
        (LUNDI,    'Lundi'       ),
        (MARDI,    'Mardi'       ),
        (MERCREDI, 'Mercredi'    ),
        (JEUDI,    'Jeudi'       ),
        (VENDREDI, 'Vendredi'    ),
        (SAMEDI,   'Samedi'      ),
        (DIMANCHE, 'Dimanche'    ),
    )
    
    day             = models.CharField("Jour", max_length=10, choices=WEEKDAY_CHOICES)
    
    def __str__(self):
        return self.day

    class Meta:
            verbose_name = "Jour"
            verbose_name_plural = "Jours"
            
            

class Period(models.Model):
    
    period          = models.CharField("Période", max_length=20, null=False)
    
    def __str__(self):
        return self.period

    class Meta:
            verbose_name = "Période"
            verbose_name_plural = "Périodes"
            
            

class Host(models.Model):
    
    firstname   = models.CharField("Prénom", max_length=100, null=True)
    lastname    = models.CharField("Nom", max_length=100, null=True)
    initials    = models.CharField("Initiales", max_length=10, null=True)
    image       = models.ImageField("Image", upload_to="images/hosts/", default = "noimage.jpg")
    resume      = models.TextField("Présentation",null=True)
    
    def __str__(self):
        return '%s %s' % (self.firstname, self.lastname)

    class Meta:
            verbose_name = "Animateur"
            verbose_name_plural = "Animateurs"



class Age_Class(models.Model):
    
    age_class    = models.CharField("Classe d'age", max_length=100, null=False)
    
    def __str__(self):
        return self.age_class

    class Meta:
            verbose_name = "Age - Classe d'ages"
            verbose_name_plural = "Age - Classes d'ages"



class Age_Group(models.Model):
    
    age_group   = models.ForeignKey(Age_Class, related_name="Age_Group", on_delete=models.SET_NULL, null=True)
    age_min     = models.IntegerField("Age minimum", null=False)
    age_max     = models.IntegerField("Age maximum", null=False)
    
    def __str__(self):
        return '%s - %s - %s' % (self.age_group, str(self.age_min), str(self.age_max))

    class Meta:
            verbose_name = "Age - Groupe d'ages"
            verbose_name_plural = "Age - Groupes d'ages"
            


class Level(models.Model):
    
    level           = models.CharField("Niveau", max_length=100, null=False)
    
    def __str__(self):
        return self.level

    class Meta:
            verbose_name = 'Niveau'
            verbose_name_plural = 'Niveaux'



class City(models.Model):
    
    city            = models.CharField("Ville", max_length=100, null=False)

    def __str__(self):
        return self.city
        
    class Meta:
            verbose_name = "Ville"
            verbose_name_plural = "Villes"
            
            

class Venue(models.Model):
    
    name            = models.CharField("Nom", max_length=100, null=False)
    street_nb       = models.CharField("N°", max_length=20,  null=False)
    street_name     = models.CharField("Rue", max_length=200, null=False)
    city            = models.ForeignKey(City, related_name="Venue", on_delete=models.SET_NULL, null=True)
    postcode        = models.IntegerField("Code Postal", null=False)
    iframe_url_map  = models.URLField("URL Google Iframe", max_length=500,  null=True)
    
    
    def __str__(self):
        return self.name

    class Meta:
            verbose_name = 'Lieu'
            verbose_name_plural = 'Lieux'


class Room(models.Model):
    
    venue           = models.ForeignKey(Venue, related_name="Room", on_delete=models.SET_NULL, null=True)
    room            = models.CharField("Salle", max_length=100, null=False)
    
    def __str__(self):
        return '%s - Salle %s' % (self.venue, self.room)

    class Meta:
        verbose_name = 'Salle'
        verbose_name_plural = 'Salles'
        


class Event(models.Model):
    
    event_type        = models.ForeignKey(Event_Type, related_name="Event",          on_delete=models.SET_NULL, null=True)
    animation         = models.ForeignKey(Animation,  related_name="Event",          on_delete=models.SET_NULL, null=True)
    name              = models.CharField("Nom", max_length=100)
    period            = models.ForeignKey(Period,     related_name="Event",          on_delete=models.SET_NULL, null=True)
    host_1            = models.ForeignKey(Host,       related_name="Event_host_1",   on_delete=models.SET_NULL, null=True)
    host_2            = models.ForeignKey(Host,       related_name="Event_host_2",   on_delete=models.SET_NULL, null=True)
    host_3            = models.ForeignKey(Host,       related_name="Event_host_3",   on_delete=models.SET_NULL, null=True)
    host_4            = models.ForeignKey(Host,       related_name="Event_host_4",   on_delete=models.SET_NULL, null=True)
    host_5            = models.ForeignKey(Host,       related_name="Event_host_5",   on_delete=models.SET_NULL, null=True)
    day               = models.ForeignKey(Weekday,    related_name="Event",          on_delete=models.SET_NULL, null=True)
    time_start        = models.TimeField("Heure de début", null=True)
    time_end          = models.TimeField("Heure de fin",   null=True)
    # dates             = ArrayField(models.DateTimeField(auto_now=False, auto_now_add=False))
    age_group         = models.ForeignKey(Age_Group,  related_name="Event",          on_delete=models.SET_NULL, null=True)
    level             = models.ForeignKey(Level,      related_name="Event",          on_delete=models.SET_NULL, null=True)
    room              = models.ForeignKey(Room,       related_name="Event",          on_delete=models.SET_NULL, null=True)
    number_max        = models.PositiveSmallIntegerField("Nb max participants", null=True)
    number_available  = models.PositiveSmallIntegerField("Nb places libres", null=True)
    rate_resident     = models.DecimalField("Tarif MC", max_digits=6, decimal_places=2, null=True)
    rate_non_resident = models.DecimalField("Tarif hors MC", max_digits=6, decimal_places=2, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Elément'
        verbose_name_plural = 'Eléments'
        
        
        
class EventRegistration(models.Model):
    
    participant         = models.ForeignKey(User, related_name="RegistrationList",  on_delete=models.PROTECT, null=False)
    event               = models.ForeignKey(Event, related_name="RegistrationList", on_delete=models.PROTECT, null=False)
    
    class Meta:
        unique_together = ["participant", "event"]
    
    def __str__(self):
        return 'Event Registration N° %s' % (self.id)
    
    class Meta:
        verbose_name = 'Inscription'
        verbose_name_plural = 'Inscriptions'
        
# ----------------------------------------------------------------------

    # It's possible to define a function to automatically fill a field : 
    # @property
    # def banana_1(self):
    #     return "This is the value"
    
    # @property
    # def banana_2(self):
    #     return "This is the value"