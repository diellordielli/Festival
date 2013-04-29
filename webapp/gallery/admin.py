import models
from django.contrib import admin
from django.contrib.auth.models import User


class ImageAdmin(admin.ModelAdmin):
    model = models.Image
    list_display = ('name', 'band', 'year', 'is_yearcover',)
    search_fields = ('name', 'band', 'year',)
    list_filter = ('name', 'band', 'year',)


admin.site.register(models.Image, ImageAdmin)
