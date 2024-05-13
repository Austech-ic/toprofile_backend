from django.db import models
import uuid
import re
from .constant import STATUS

SPECIAL_CHARS_REGEX = "[^a-zA-Z0-9 \n\.]"
class ListingCategory(models.Model):
    name=models.CharField(max_length=100,null=False)
# Create your models here.
class Blog(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    title=models.TextField(null=True)
    body=models.TextField(null=False,blank=False)
    status=models.CharField(choices=STATUS,default="published",max_length=10)
    image=models.ImageField(upload_to=upload_to,null=True)
    read_min=models.CharField(max_length=300,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

class PropertyListing(models.Model):
    description=models.TextField()
    category=models.ForeignKey(ListingCategory,on_delete=models.CASCADE,null=True,blank=True)
    content=models.TextField()
    place=models.CharField(max_length=500,null=True)
    address=models.CharField(max_length=500,null=True)
    status=models.CharField(choices=STATUS,default="published",max_length=10)
    duration=models.IntegerField(default=0)
    land_space=models.IntegerField(default=0)
    price=models.DecimalField(max_digits=10,decimal_places=0)
    no_bedroom=models.IntegerField(default=0)
    no_bathroom=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)

class ImageAsset(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    image=models.ImageField(upload_to=upload_to)
    property=models.ForeignKey(PropertyListing,on_delete=models.CASCADE,null=True,blank=True)

class HomePage(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    background_image=models.ImageField(upload_to=upload_to,null=True)
    title=models.TextField()
    content=models.TextField(null=True)
    location=models.CharField(max_length=500,null=True)
    phone_number=models.TextField(null=True)
    email_link=models.URLField(null=True)

#PrivatePolicy
class PrivatePolicy(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()
#Terms and Services
class TermsOfService(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()
#About Us
class AboutUs(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/about/{filename}".format(filename=filename),
        )
        return url
    image=models.ImageField(upload_to=upload_to,null=True)
    about=models.TextField()

class OurServices(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/services/{filename}".format(filename=filename),
        )
        return url
    image=models.ImageField(upload_to=upload_to,null=True)
    title=models.CharField(max_length=500)
    content=models.TextField()

class Statement(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()

class OurTeam(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    image=models.ImageField(upload_to=upload_to,null=True)
    name=models.TextField(null=True)
    title=models.CharField(max_length=500,null=False)
    facebook_link=models.URLField()
    instagram_link=models.URLField()
    email_link=models.URLField()
    twitter_link=models.URLField()

class Testimony(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    name=models.TextField()
    comment=models.TextField()
    status=models.CharField(choices=STATUS,default="draft",max_length=10)
    image=models.ImageField(upload_to=upload_to,null=True)
    created_at=models.DateTimeField(auto_now_add=True)


class FillContactForm(models.Model):
    full_name=models.TextField()
    email=models.EmailField()
    message=models.TextField()


class Agent(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    image=models.ImageField(upload_to=upload_to,null=True)
    name=models.TextField(null=True)
    title=models.CharField(max_length=500,null=False)
    facebook_link=models.URLField()
    instagram_link=models.URLField()
    email_link=models.URLField()
    twitter_link=models.URLField()