# -*- coding: utf-8 -*-
from django.db import models


class Contact(models.Model):
    category = models.CharField(max_length=200)
    email = models.EmailField(max_length=75)

    class Meta:
        verbose_name_plural = "Contacts"

    def __unicode__(self):
        return u"%s %s" % (self.category, self.email)


class Person(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField(max_length=75)
    about = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Persons"

    def __unicode__(self):
        return u"%s %s %s %s" % (self.firstname, self.lastname, self.email, self.about)
