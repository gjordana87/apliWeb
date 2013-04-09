from django.conf.urls import patterns, include, url
from escola.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apliWeb.views.home', name='home'),
    # url(r'^apliWeb/', include('apliWeb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainpage, name='home'),
    url(r'^login/$','django.contrib.auth.views.login'),

    #url(r'^base$', base, name='base'),

    #escola
    url(r'^escola/$',escola),    
    #reglament
    url(r'^reglament/$',reglament),
    #equips
    url(r'^equip/$',equip),
    #url(r'^equip/$','equip.views.equip'),
    #url(r'^equip/(?P<equip_categoria>\W+)$',equip),

    #instalacions
    url(r'^instalacions/$',instalacions),
    #detallequips
    url(r'^models/(? P <detalls> \ w +) / $', detallescoles, nom = 'Detalls del model'),
    #detallescoles
    url(r'^detallescoles/$',detallescoles),



)
