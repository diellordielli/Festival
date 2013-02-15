import models
from django.contrib import admin
from django.contrib.auth.models import User

from . import models


class MoodAdmin(admin.ModelAdmin):
    model = models.Mood
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(models.Mood, MoodAdmin)
