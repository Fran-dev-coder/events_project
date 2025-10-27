from django.contrib import admin
from .models import User, Genre, Artist, Location, Event
# Register your models here.
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Location)
admin.site.register(Event)