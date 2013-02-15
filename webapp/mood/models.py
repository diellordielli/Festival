from django.db import models


class Mood(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="mood")

    def __unicode__(self):
        return u"%s %s" % (self.name, self.description)
