from django.db                      import models
from django.contrib.postgres.fields import ArrayField
from activities.models              import Animation, Host, Age_Group, Room


class Workshop(models.Model):
    
    animation                 = models.ForeignKey(Animation,  related_name="Workshop",  on_delete=models.SET_NULL, null=True)
    host                      = models.ManyToManyField(Host,  related_name="Workshop",                                        blank=True)
    name                      = models.CharField("Nom", max_length=50,                                             null=True)
    age_group                 = models.ForeignKey(Age_Group,  related_name="Workshop",  on_delete=models.SET_NULL, null=True)
    level                     = models.TextField("Niveau",                                                         null=True, blank=True)
    dates                     = models.TextField("Dates & Horaires",                                               null=True, blank=True)
    date_of_the_last_day      = models.DateField("Date du dernier jour")
    description               = models.TextField("Description",                                                    null=True, blank=True)
    notes                     = models.TextField("Notes particulières",                                            null=True, blank=True)
    rate                      = models.TextField("Tarifs",                                                         null=True, blank=True)
    room                      = models.ForeignKey(Room,       related_name="Workshop",  on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return '%s - %s - %s' % (self.animation, self.name, self.age_group)
    
    class Meta:
        verbose_name = 'Atelier'
        verbose_name_plural = 'Ateliers'