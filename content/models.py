from django.db import models


class Type_category(models.Model):
    
    default         = "Te be determined"
    
    type_category   = models.CharField(max_length=100, default = default, null=False)
    
    def __str__(self):
        return self.type_category

class Activity(models.Model):
    
    default_leader      = 'To be determined'
    default_venue       = 'To be determined'
    default_age_range   = 'To be determined'
    default_level       = 'To be determined'
    
    name            = models.CharField(max_length=100)
    type_category   = models.ForeignKey(Type_category, related_name='activity', on_delete=models.CASCADE, null=True)
    # age_range       = models.ForeignKey(table_age_range, related_name="activity", on_delete=models.SET(default_age_range), null=False)
    # level           = models.ForeignKey(table_level, related_name="activity", on_delete=models.SET(default_level), null=False)
    description     = models.TextField()
    day             = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    # time_start      = models.TimeField(auto_now=False, auto_now_add=False)
    # time_end        = models.TimeField(auto_now=False, auto_now_add=False)
    # venue           = models.ForeignKey(table_venue,  related_name='activity', default=default_venue,  on_delete=models.SET(default_venue),  null=False)
    # leader          = models.ForeignKey(table_leader, related_name='activity', default=default_leader, on_delete=models.SET(default_leader), null=False)
    # image           = models.ImageField(upload_to="images", blank=True, null=True)
    rate            = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name
