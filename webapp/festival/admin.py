from django.contrib import admin
from django.contrib.auth.models import User

from . import models


class YearAdmin(admin.ModelAdmin):
    model = models.Year
    list_display = ('year', 'start', 'end',)
    search_fields = ('year',)
    list_filter = ('year',)


class BandYearInline(admin.TabularInline):
    model = models.BandYear
    extra = 0


class BandLinksInline(admin.TabularInline):
    model = models.BandLinks
    extra = 0


class BandAdmin(admin.ModelAdmin):
    model = models.Band
    inlines = [
        BandLinksInline,
        BandYearInline,
    ]    
    list_display = ('name', 'description', 'genre', 'get_band_years')
    search_fields = ('name', 'genre')
    list_filter = ('genre', 'bandyear__year', 'bandyear__stage')


admin.site.register(models.Band, BandAdmin)
admin.site.register(models.Year, YearAdmin)
