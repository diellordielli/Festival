# -*- coding: utf-8 -*-
from django.db import models


class News(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    time = models.DateTimeField()
    image = models.ImageField(upload_to="news", blank=True)

    class Meta:
        verbose_name_plural = "News"
        ordering = ['-time']

    def __unicode__(self):
        return u"%s %s" % (self.name, self.description)
