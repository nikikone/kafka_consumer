from django.db import models

# Create your models here.


class Zone(models.Model):
    id_zone = models.IntegerField('id области', default=0)
    in_zone = models.IntegerField('сколько вошло в область', default=0)
    out_zone = models.IntegerField('сколько вышло из области', default=0)

