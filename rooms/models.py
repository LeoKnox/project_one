from django.db import models
from django.contrib.auth.models import User

class RoomManager(models.Manager):
    def get_queryset(self):
        return super(RoomManager, self).get_queryset().filter(name='entry')

class Room(models.Model):
    ROOM_SHAPES = (
        ('square', 'Square'),
        ('octagon', 'Octagon'),
    )
    name = models.CharField(max_length=250)
    description = models.TextField()
    length = models.IntegerField()
    width = models.IntegerField()
    dm = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='dungeon_master')
    shape = models.CharField(max_length=10,
                                choices=ROOM_SHAPES,
                                default='square')
    objects = models.Manager()
    room = RoomManager()

    class Meta:
        ordering = ('-name',)
    
    def __str__(self):
        return self.name