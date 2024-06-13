from django.db import models
import uuid
import re
from .constant import STATUS

SPECIAL_CHARS_REGEX = "[^a-zA-Z0-9 \n\.]"

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
    author_name=models.CharField(max_length=300,null=True)
    image=models.ImageField(upload_to=upload_to,null=True)
    reading_time=models.CharField(max_length=300,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

class PropertyListing(models.Model):
    body=models.TextField()
    title=models.TextField()
    address=models.CharField(max_length=500,null=True)
    land_space=models.IntegerField(default=0)
    amount=models.DecimalField(max_digits=10,decimal_places=0)
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

class HeroSection(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    heading=models.TextField()
    sub_heading=models.TextField()
    image=models.ImageField(upload_to=upload_to,null=True)

class FeatureSection(models.Model):
    heading=models.TextField()
    sub_heading=models.TextField()

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
    first_name=models.CharField(null=True,max_length=500)
    last_name=models.TextField(null=True,max_length=500)
    postion=models.TextField(null=True,max_length=500)
    facebook_link=models.URLField()
    instagram_link=models.URLField()
    email_link=models.URLField()
    twitter_link=models.URLField()


class FillContactForm(models.Model):
    full_name=models.TextField()
    email=models.EmailField()
    message=models.TextField()

#done
class AgentMember(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/profile/{filename}".format(filename=filename),
        )
        return url
    name=models.TextField(null=False)
    image=models.ImageField(upload_to=upload_to,null=True)
    facebook_link=models.URLField(null=True)
    instagram_link=models.URLField(null=True)
    email_link=models.URLField(null=True)
    twitter_link=models.URLField(null=True)

class Agent(models.Model):
    heading=models.TextField(null=True)
    sub_heading=models.CharField(max_length=500,null=False)
    agent=models.ManyToManyField(AgentMember,related_name="agents")


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
    image=models.ImageField(upload_to=upload_to,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

#PrivatePolicy
class PrivatePolicy(models.Model):
    content=models.TextField()
#Terms and Services
class TermsOfService(models.Model):
    content=models.TextField()


class AdminAppearance(models.Model):
    def upload_to(instance, filename):
        url = re.sub(
            SPECIAL_CHARS_REGEX,
            "_",
            "images/admin/{filename}".format(filename=filename),
        )
        return url
    logo=models.ImageField(upload_to=upload_to,null=True)
    icon=models.ImageField(upload_to=upload_to,null=True)
    background=models.ImageField(upload_to=upload_to,null=True)