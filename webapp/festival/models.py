# -*- coding: utf-8 -*-
from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=200, help_text="Trenne Genres mit '/'")
    image = models.ImageField(upload_to="bands", blank=True)
    slug = models.SlugField(default="-")

    def __unicode__(self):
        return u"%s" % (self.name)

    def get_band_years(self):
        answer = ""

        for by in self.bandyear_set.all():
            answer += '%s %s %s' % (by.year, by.get_stage_display(), by.time) + ', '
        return answer

    def get_stage_time(self):
        """ gets the next or last stage time """

        bandyear = self.bandyear_set.latest('time')

        if bandyear:
            return bandyear.time
        else:
            return None

    def dotted_genres(self):
        return u' • '.join(self.genre.split('/'))

    @models.permalink
    def get_absolute_url(self):
        return ("get_band", (), {"band": self.slug})


class BandLinks(models.Model):
    FACEBOOK = "FB"
    WEBSITE = "WS"
    MYSPACE = "MS"
    SOUNDCLOUD = "SC"
    YOUTUBE = "YT"
    TWITTER = "TT"

    LINK_TYPES = (
        (FACEBOOK, 'Facebook'),
        (WEBSITE, 'Website'),
        (MYSPACE, 'MySpace'),
        (SOUNDCLOUD, 'Soundcloud'),
        (YOUTUBE, 'Youtube'),
        (TWITTER, 'Twitter'),
    )

    link = models.URLField()
    type = models.CharField(max_length=20, choices=LINK_TYPES, default=WEBSITE)
    band = models.ForeignKey(Band)

    class Meta:
        verbose_name_plural = "Band Links"

    def __unicode__(self):
        return u"%s %s" % (self.link, self.band)


class Year(models.Model):
    year = models.PositiveSmallIntegerField()
    start = models.DateField()
    end = models.DateField()
    logo = models.ImageField(upload_to="years", blank=True)
    bands = models.ManyToManyField(Band, related_name="years", through="BandYear")

    class Meta:
        ordering = ["year"]

    def __unicode__(self):
        return u"%s" % (self.year)

    @models.permalink
    def get_gallery_url(self):
        return ("get_gallery", (), {"year": self.year})


class BandYear(models.Model):
    HAUPTBUEHNE = "HB"
    ZELTBUEHNE = "ZB"

    LINK_TYPES = (
        (HAUPTBUEHNE, 'Hauptbühne'),
        (ZELTBUEHNE, 'Zeltbühne'),
    )

    stage = models.CharField(max_length=20, choices=LINK_TYPES)
    time = models.DateTimeField()
    band = models.ForeignKey(Band)
    year = models.ForeignKey(Year)

    class Meta:
        verbose_name_plural = "Band Years"

    def __unicode__(self):
        return u"%s %s" % (self.stage, self.band)