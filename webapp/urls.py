from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^webapp/', include('webapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Home
    url(r'^$', 'webapp.views.home', name='home'),

    # Bandsingle
    url(r'^band/(?P<band>[-a-z0-9]+)/$', 'webapp.views.get_band', name='get_band'),

    # Gallery
    url(r'^gallery/(?P<year>\d+)/$', 'webapp.views.get_gallery', name='get_gallery'),

    # Forms
    url(r'^contact/$', 'webapp.views.contact', name='contact'),

    url(r'^thanks/$', 'webapp.views.thanks', name='thanks'),

)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^upload/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
    )
