import models
from django.contrib import admin
from django.contrib.auth.models import User


class SponsorCategoryYearInline(admin.TabularInline):
    model = models.SponsorCategoryYear
    extra = 0


class SponsorAdmin(admin.ModelAdmin):
    model = models.Sponsor
    inlines = [
        SponsorCategoryYearInline,
    ]
    list_display = ('name', 'link','get_sponsor_years')
    search_fields = ('name',)
    list_filter = ('years', 'sponsorcategoryyear__category')


class CategoryAdmin(admin.ModelAdmin):
    model = models.Category
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(models.Sponsor, SponsorAdmin)
admin.site.register(models.Category, CategoryAdmin)
