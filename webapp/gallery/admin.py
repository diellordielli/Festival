import models
from django.contrib import admin
from django.contrib.auth.models import User

class CategoryAdmin(admin.ModelAdmin):
    model = models.Category


class ImageAdmin(admin.ModelAdmin):
    model = models.Image


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Image, ImageAdmin)
