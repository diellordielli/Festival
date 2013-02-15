import models
from django.contrib import admin
from django.contrib.auth.models import User

from . import models


class NewsAdmin(admin.ModelAdmin):
    model = models.News
    list_display = ('name', 'time',)
    search_fields = ('name',)
    list_filter = ('time',)


admin.site.register(models.News, NewsAdmin)
