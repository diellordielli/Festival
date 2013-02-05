from django.db import models

from ..festival.models import Band, Year


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return u"%s %s" % (self.name, self.description)


class Image(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="gallery")
    date = models.DateTimeField()
    band = models.ForeignKey(Band, related_name="images", null=True)
    year = models.ForeignKey(Year)
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return u"%s %s %s" % (self.name, self.band, self.description)
