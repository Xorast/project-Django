from django.db import models


def upload_path_handler(instance, filename):
    return "images/events/{family}/{title}/{file}".format(family=instance.family, title=instance.title, file=filename)


class Event_Family(models.Model):
    
    family = models.CharField("Famille d'événements (PAS DE SLASH DANS LE NOM !)", max_length=50, null=False,
                              blank=False, unique=True)
    image = models.ImageField("Image", upload_to="images/event_family/", blank=True, null=True)

    def __str__(self):
            return self.family
        
    class Meta:
        verbose_name = "Famille d'événements"
        verbose_name_plural = "1. Familles d'événements"

            
class Event(models.Model):
    
    family = models.ForeignKey(Event_Family,  related_name="Event",  on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField("Titre (nom)", max_length=100, null=False, blank=False)
    subtitle = models.CharField("Sous-titre",  max_length=100, null=False, blank=True)
    description = models.TextField("Description", null=True, blank=False)
    venue = models.CharField("Lieu(x)",  max_length=100, null=False, blank=False)
    date_and_time = models.CharField("Date(s) & Heure(s)",  max_length=200, null=True, blank=False)
    date_first_day = models.DateField("Commence le", null=True)
    date_last_day = models.DateField("Finit le ", null=True)
    image = models.ImageField("Image", upload_to=upload_path_handler, blank=True, null=True)
    notes = models.CharField("Notes",  max_length=100, null=False, blank=True)
    bubble_info = models.TextField("Bulle info", null=True, blank=True)
    contact = models.CharField("Personne à contacter",  max_length=100, null=True, blank=True)
    rate = models.CharField("Tarifs", max_length=100, null=True, blank=True)
    file = models.FileField("PDF", upload_to='files/events/', null=True, blank=True)
        
    def __str__(self):
        return '%s - %s - %s' % (self.family, self.title, self.date_first_day)
    
    class Meta:
        verbose_name = "Evénement"
        verbose_name_plural = "2. Evénements"
