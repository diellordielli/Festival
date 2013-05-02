import models
from django.contrib import admin
from django.contrib.auth.models import User


class ImageAdmin(admin.ModelAdmin):
    model = models.Image
    list_display = ('name', 'choice', 'year', 'is_yearcover', 'image')
    search_fields = ('name', 'band', 'year',)
    list_filter = ('year', 'name', 'band',)


admin.site.register(models.Image, ImageAdmin)
