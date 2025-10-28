from django.contrib import admin
from .models import User, Genre, Artist, Location, Event

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','is_seller','phone_number','referral_code')
    list_filter = ('is_seller',)
    search_fields = ('username','email','referral_code')

@admin.register(Genre)  
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'genres__name')
    list_filter = ('genres',)
    filter_horizontal = ('genres',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name','address','capacity')
    search_fields = ('name','address')
    list_filter = ('capacity',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'date', 'location_name')
    list_filter = ('date', 'location')
    search_fields = ('event_name',)
    filter_horizontal = ('artists',)

    def location_name(self, obj):
        return obj.location.name
    location_name.short_description = 'Location'