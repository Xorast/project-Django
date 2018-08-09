from django.db                  import models
from django.utils               import timezone



class News(models.Model):
    """
    A single Blog post
    """
    title           = models.CharField(max_length=200)
    content         = models.TextField()
    created_date    = models.DateTimeField(auto_now_add=True)
    published_date  = models.DateTimeField(blank=True, null=True, default=timezone.now)
    tag             = models.CharField(max_length=30, blank=True, null=True)
    image           = models.ImageField(upload_to="images", blank=True, null=True)
    
    def __str__(self):
        return self.title