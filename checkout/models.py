from django.db                      import models
from django.contrib.auth.models     import User
from activities.models              import Event

class RegistrationOrder(models.Model):
    
    user        = models.ForeignKey(User,  on_delete=models.CASCADE, related_name="RegistrationOrder")
    event       = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="RegistrationOrder")
    date        = models.DateField(auto_now_add=True)
    paid_fare   = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.event, self.user)
    
    class Meta:
        verbose_name = 'Paiement'
        verbose_name_plural = 'Paiements'
        
class User(models.Model):
    
    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'tests'