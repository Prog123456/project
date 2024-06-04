from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TimeIn(models.Model):
    
    clicked_date = models.DateField(auto_now_add=True,null=True)
    clicked_time = models.TimeField(auto_now=True,null=True)
class BreakInMorning(models.Model):
    
    clicked_date = models.DateField(auto_now_add=True,null=True)
    clicked_time = models.TimeField(auto_now=True,null=True)

class BreakOutMorning(models.Model):
    
    clicked_date = models.DateField(auto_now_add=True,null=True)
    clicked_time = models.TimeField(auto_now=True,null=True)

class LunchIn(models.Model):
    
    clicked_date = models.DateField(auto_now_add=True,null=True)
    clicked_time = models.TimeField(auto_now=True,null=True)

class LunchOut(models.Model):
    
    clicked_date = models.DateField(auto_now_add=True,null=True)
    clicked_time = models.TimeField(auto_now=True,null=True)
class BreakInNoon(models.Model):
    
    clicked_date = models.DateField(auto_now_add=True,null=True)
    clicked_time = models.TimeField(auto_now=True,null=True)

class BreakOutNoon(models.Model):
    
    clicked_date = models.DateField(auto_now_add=True,null=True)
    clicked_time = models.TimeField(auto_now=True,null=True)

class TimeOut(models.Model):
    
    clicked_date = models.DateField(auto_now_add=True,null=True)
    clicked_time = models.TimeField(auto_now=True,null=True)
