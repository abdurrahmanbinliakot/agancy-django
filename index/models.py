from django.db import models

# Create your models here.

class Services(models.Model):
    ICON_TYPE = (
        ('laptop','laptop'),
        ('camera','camera'),
        ('book','book'),
    )

    service_heading = models.TextField(max_length=30,blank=False)
    service_description = models.TextField(max_length=100,blank=False)
    service_icon = models.CharField(max_length=20,choices=ICON_TYPE)

# Create your models here.
class Portfolio(models.Model):
    portfolio_heading = models.TextField(max_length=50,blank=False)
    portfolio_sub_heading = models.TextField(max_length=100,blank=False)
    portfolio_image = models.ImageField(upload_to='portfolio_images')


# Create your models here.
class About(models.Model):
    date =models.TextField(max_length=20,blank=True)
    about_heading = models.TextField(max_length=30,blank=False)
    about_description = models.TextField(max_length=200,blank=False)
    about_image = models.ImageField(upload_to='about_images')


# Create your models here.
class TeamMember(models.Model):
    name =models.TextField(max_length=30,blank=False)
    designation =models.TextField(max_length=100,blank=False)
    photo = models.ImageField(upload_to='team_member_photo',blank=False)
    facebook_profile = models.URLField()
    twitter_profile = models.URLField()
    linkedin_profile = models.URLField()

# Create your models here for Clients.
class Clients(models.Model):
    client_name =models.TextField(max_length='50',blank=False)
    client_url =models.URLField()
    client_logo =models.ImageField(upload_to='clients_url')