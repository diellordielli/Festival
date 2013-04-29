from django.db import models

from ..festival.models import Band, Year


class Image(models.Model):
    FESTIVAL = "Festival"
    BANDS = "Bands"

    LINK_TYPES = (
        (FESTIVAL, 'Festival'),
        (BANDS, 'Bands'),
    )

    choice = models.CharField(max_length=20, choices=LINK_TYPES)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="gallery")
    date = models.DateTimeField()
    band = models.ForeignKey(Band, related_name="images", null=True, blank=True)
    year = models.ForeignKey(Year)
    is_yearcover = models.BooleanField(default=False)

    def clean(self):
        if self.is_yearcover:
            self.year.image_set.filter(is_yearcover=True)\
                    .update(is_yearcover=False)

    def __unicode__(self):
        return u"%s %s %s %s" % (self.choice,  self.name, self.band, self.description)
