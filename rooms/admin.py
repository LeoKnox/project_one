from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'width', 'length', 'shape', 'dm')
    list_filter = ('name', 'width', 'length', 'dm')
    search_fields = ('name', 'dm')
    ordering = ('name', 'dm')