from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


# LOW = 1
# MID = 2
# HIGH = 3
# CHOICES = (
#     (LOW, 'Low')
#     (MID, 'Medium')
#     (HIGH, 'High')
# )


class Champion(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    damage = models.IntegerField(choices=list(zip(range(1,4), range(1,4))), default=0)
    utlity = models.IntegerField(choices=list(zip(range(1,4), range(1,4))), default=0)
    toughness = models.IntegerField(choices=list(zip(range(1,4), range(1,4))), default=0)
    difficulty = models.IntegerField(choices=list(zip(range(1,4), range(1,4))), default=0)

    class Champion_type(models.TextChoices):
        Controller = 'Controller', _('Controller'),
        Fighter = 'Fighter', _('Fighter'),
        Mage = 'Mage', _('Mage'),
        Marksman = 'Marksman', _('Marksman'),
        Slayer = 'Slayer', _('Slayer')
        Tank = 'Tank', _('Tank')
        Default = 'Noob', _('Noob')

    champ_type = models.CharField(
        max_length=20,
        choices=Champion_type.choices,
        default=Champion_type.Default,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
