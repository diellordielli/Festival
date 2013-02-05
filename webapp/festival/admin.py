from django.contrib import admin
from django.contrib.auth.models import User

from . import models


class YearAdmin(admin.ModelAdmin):
    model = models.Year


class BandYearInline(admin.TabularInline):
    model = models.BandYear
    extra = 0


class SponsorCategoryYearInline(admin.TabularInline):
    model = models.SponsorCategoryYear
    extra = 0



class SponsorAdmin(admin.ModelAdmin):
    model = models.Sponsor
    inlines = [
        SponsorCategoryYearInline,
    ]
    list_display = ('name', 'link',)


class CategoryAdmin(admin.ModelAdmin):
    model = models.Category
    list_display = ('name',)
    list_filter = ('name',)


class BandLinksInline(admin.TabularInline):
    model = models.BandLinks
    extra = 0

class BandAdmin(admin.ModelAdmin):
    model = models.Band
    inlines = [
        BandLinksInline,
        BandYearInline,
    ]    
    list_display = ('name', 'description', 'genre', 'image')
    search_fields = ('name', 'genre')
    list_filter = ('genre',)


admin.site.register(models.Band, BandAdmin)
admin.site.register(models.Year, YearAdmin)
admin.site.register(models.Sponsor, SponsorAdmin)
admin.site.register(models.Category, CategoryAdmin)
