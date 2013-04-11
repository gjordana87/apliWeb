from django.conf.urls import patterns, include, url
from escola.views import mainpage, escola, reglament, equip, instalacions, detallescoles, detallequips, detallinstall,detallreglament
from escola.views import login_view, logout_view, base
# Uncomment the next two lines to enable the admin:from django.contrib.auth.models import User

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apliWeb.views.home', name='home'),
    # url(r'^apliWeb/', include('apliWeb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', mainpage),
    url(r'^login/$','escola.views.login_view',name='vista_login'),
    url(r'^logout/$','escola.views.logout_view',name='vista_logout'),

    #url(r'^base$', base, name='base'),

    #escola
    url(r'^escola/$',escola),
    url(r'^base/$',base),    
    
    #reglament
    url(r'^reglament/$',reglament),
    #equips
    url(r'^equip/$',equip),
    #url(r'^equip/$','equip.views.equip'),
    #url(r'^equip/(?P<equip_categoria>\W+)$',equip),

    #instalacions
    url(r'^instalacions/$',instalacions),
    
    url(r'^detallescoles/(?P<idEscole>\w+)',detallescoles),
    url(r'^detallequips/(?P<idEquip>\w+)',detallequips),
    url(r'^detallinstall/(?P<idInstalacions>\w+)',detallinstall),
    url(r'^detallreglament/(?P<idReglament>\w+)',detallreglament),
    
    url(r'^detallescoles/$',detallescoles),
    url(r'^detallequips/$',detallequips),
    url(r'^detallinstall/$',detallinstall),
    url(r'^detallreglament/$',detallreglament),




    url(r'^admin/', include(admin.site.urls)),
)
