from django.db import models
from djang.contriib.dungon.models import Dungeon

class Post(models.Model):
    ROOM_SHAPES = (
        ('square', 'Square'),
        ('octagon', 'Octagon'),
    )
    name = models.CharField(max_length=250)
    description = models.TextField()
    length = models.IntegerField()
    width = models.IntegerField()
    dungeon = models.ForeignKey(Dungeon,
                                on_delete=models.CASCADE,
                                related_name='dungeon_name')
    shape = models.CharField(max_length=10,
                                choices=ROOM_SHAPES,
                                default='square')
                                
    class Meta:
        order = ('-name')
    
    def __str__(self):
        return self.name