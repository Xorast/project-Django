from django.db import models

class Slides(models.Model):
    
    slide_title      = models.CharField("Diapo - Titre", max_length=100, null=False, blank=False)
    slide_subtitle   = models.CharField("Diapo - Sous titre", max_length=4, null=False, blank=False)
    image            = models.ImageField("Diapo - Image", upload_to="images/carousel", blank=True, null=True)
    
    def __str__(self):
            return 'Diapositive %s' % (str(self.id))
        
    class Meta:
        verbose_name = "1. Diapositives"
        verbose_name_plural = "Caroussel"