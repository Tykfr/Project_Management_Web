from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.shortcuts import reverse
# Create your models here.

class CustomUser(AbstractUser):
    pass
    # add additional fields here
    def full_name(self):
        return self.first_name + " " + self.last_name
    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.id

class Profile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    age = models.IntegerField(null=True,blank=True)
    description = models.CharField(max_length=250,null=True,blank=True)
    photo = models.ImageField(upload_to='profile_image',null=True,blank=True)

    def __unicode__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('profile')


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
