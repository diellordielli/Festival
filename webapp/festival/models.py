from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    image = models.ImageField(upload_to="bands")

    def __unicode__(self):
        return u"%s" % (self.name)
    

class BandLinks(models.Model):
    FACEBOOK = "FB"
    WEBSITE = "WS"

    LINK_TYPES = (
        (FACEBOOK, 'Facebook'),
        (WEBSITE, 'Website'),
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
    logo = models.ImageField(upload_to="years")
    bands = models.ManyToManyField(Band,
        related_name="years", through="BandYear")

    def __unicode__(self):
        return u"%s" % (self.year)


class BandYear(models.Model):
    stage = models.CharField(max_length=200)
    time = models.DateTimeField()
    band = models.ForeignKey(Band)
    year = models.ForeignKey(Year)

    class Meta:
        verbose_name_plural = "Band Years"

    def __unicode__(self):
        return u"%s %s" % (self.stage, self.band)


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="sponsors")
    link = models.URLField(max_length=200)
    years = models.ManyToManyField(Year,
        related_name="sponsors", through="SponsorCategoryYear")

    def __unicode__(self):
        return u"%s %s" % (self.name, self.link)


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return u"%s" % (self.name)


class SponsorCategoryYear(models.Model):
    sponsor = models.ForeignKey(Sponsor)
    category = models.ForeignKey(Category)
    year = models.ForeignKey(Year)

    class Meta:
        verbose_name_plural = "Sponsor Categories Years"

    def __unicode__(self):
        return u"%s %s" % (self.sponsor, self.category)


