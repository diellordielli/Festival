from django.contrib import admin
from django.contrib.auth.models import User

from . import models


class YearAdmin(admin.ModelAdmin):
    model = models.Year
    list_display = ('year', 'start', 'end',)
    search_fields = ('year',)
    list_filter = ('year',)


admin.site.register(models.Band, BandAdmin)
admin.site.register(models.Year, YearAdmin)
