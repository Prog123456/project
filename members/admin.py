# Register your models here.
from django.contrib import admin
from .models import TimeIn,LunchIn,LunchOut,TimeOut,BreakInMorning,BreakOutMorning,BreakInNoon,BreakOutNoon

admin.site.register(TimeIn)
admin.site.register(BreakInMorning)
admin.site.register(BreakOutMorning)
admin.site.register(LunchIn)
admin.site.register(LunchOut)
admin.site.register(BreakInNoon)
admin.site.register(BreakOutNoon)
admin.site.register(TimeOut)