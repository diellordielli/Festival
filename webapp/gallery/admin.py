import models
from django.contrib import admin
from django.contrib.auth.models import User

class CategoryAdmin(admin.ModelAdmin):
    model = models.Category
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class ImageAdmin(admin.ModelAdmin):
    model = models.Image
    list_display = ('name', 'band', 'year', 'is_yearcover',)
    search_fields = ('name', 'band', 'year',)
    list_filter = ('name', 'band', 'year',)


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Image, ImageAdmin)
