from django.contrib import admin


from . import models


class ContactAdmin(admin.ModelAdmin):
    model = models.Contact
    list_display = ('category',)
    search_fields = ('category',)
    list_filter = ('category',)


class PersonAdmin(admin.ModelAdmin):
    model = models.Person
    list_display = ('firstname',)
    search_fields = ('firstname', 'lastname')
    list_filter = ('firstname',)


admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Person, PersonAdmin)
