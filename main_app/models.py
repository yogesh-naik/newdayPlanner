from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

TAG_CHOICES = (
    ('personal','PERSONAL'),
    ('family', 'FAMILY'),
)

class Task(models.Model):

    name = models.CharField(max_length=250)
    tag = models.CharField(max_length=10,choices=TAG_CHOICES, default='personal')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField(max_length=500, blank=True)
    
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()
        
    
    
