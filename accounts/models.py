from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=20, null=True, blank=True)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    about_bio = models.TextField(null=True, blank=True)
    career_obj = models.TextField(null=True, blank=True)
    fav_quote = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    # social media
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    x = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    discord = models.URLField(null=True, blank=True)
    messenger = models.URLField(null=True, blank=True)