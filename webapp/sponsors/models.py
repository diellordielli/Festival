from django.db import models

from ..festival.models import Year


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="sponsors")
    link = models.URLField(max_length=200)
    years = models.ManyToManyField(Year,
        related_name="sponsors", through="SponsorCategoryYear")

    def __unicode__(self):
        return u"%s %s" % (self.name, self.link)

    def get_sponsor_years(self):
        answer = ""

        for scy in self.sponsorcategoryyear_set.all():
            answer += '%s %s' % (scy.year, scy.category) + ', '
        return answer

    def get_sponsor_category(self):

        category = self.categories.latest("sponsorcategoryyear__year__year")

        if category:
            return category.name
        else:
            return None


class Category(models.Model):
    name = models.CharField(max_length=200)
    sponsors = models.ManyToManyField(Sponsor, related_name="categories",
        through="SponsorCategoryYear")

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return u"%s" % (self.name)


class SponsorCategoryYear(models.Model):
    sponsor = models.ForeignKey(Sponsor)
    category = models.ForeignKey(Category)
    year = models.ForeignKey(Year)

    class Meta:
        verbose_name_plural = "Sponsor Categories Years"

    def __unicode__(self):
        return u"%s %s" % (self.year, self.category)
