from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address_user')
    state = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    alley = models.CharField(max_length=200)
    plaque = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    extra_comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.state} / {self.city} / {self.street}"


class Skill(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False,unique=True)

    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    address = models.ManyToManyField(Address, related_name='profile_address')
    bio = models.TextField(blank=True, null=True)
    skill = models.ManyToManyField(Skill, related_name='profile_skill')
    score = models.IntegerField(default=0)
    balance = models.IntegerField(default =0)
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
   

    def get_profile_images(self):
      
        images_url = []
        for profile_image in self.profileImage_profile.all():
            images_url.append( {'image':profile_image.image.url})
        return list(images_url)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



class ProfileImage(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name='profileImage_profile')
    image = models.FileField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return self.profile.user.username
    