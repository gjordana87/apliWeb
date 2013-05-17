from django.conf.urls import patterns, include, url
from escola.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import DetailView, ListView, UpdateView


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
    url(r'^logout/$', 'django.contrib.auth.views.logout',{ 'next_page' : '/'}),
    url(r'^login/$','django.contrib.auth.views.login'),
    #url(r'^login/$',login),

    #escolaInstalacio
    url(r'^escola/$',escola),
        
    #reglament
    url(r'^reglament/$',reglament),
    #equips
    url(r'^equip/$',equip),

    #instalacions
    url(r'^instalacions/$',instalacions),

    url(r'^detallescoles/$',detallescoles),
    url(r'^detallequips/$',detallequips),
    url(r'^detallinstall/$',detallinstall),
    url(r'^detallreglament/$',detallreglament),
    
    url(r'^detallescoles/(?P<idEscole>\w+)/',detallescoles, name='detail_escola'),
    url(r'^detallequips/(?P<idEquip>\w+)/',detallequips, name='detail_equip'),
    url(r'^detallinstall/(?P<idInstalacions>\w+)/',detallinstall, name='detail_instal'),
    url(r'^detallreglament/(?P<idReglament>\w+)/',detallreglament, name='detail_regla'),


   # Crear Escola, equip, reglament, instalacions 
    url(r'^escola/Crear/$',EscolaCreate.as_view(),  name='escola_create'),
    url(r'^equip/Crear/$',EquipCreate.as_view(),name='equip_create'),
    url(r'^reglament/Crear/$',ReglamentCreate.as_view(),name='reglament_create'),
    url(r'^instalacions/Crear/$',InstalacioCreate.as_view(),name='instalacio_create'),
    #   Edit    restaurant  details,    ex.:/myrestaurants/restaurants/1/edit/
    url(r'^escola/(?P<pk>\d+)/edit/$',UpdateView.as_view(model = Escole,template_name = 'form.html',form_class = EscolaForm),name='escola_edit'),
    url(r'^equip/(?P<pk>\d+)/edit/$',UpdateView.as_view(model = Equip,template_name = 'form.html',form_class = EquipForm),name='equip_edit'),

    url(r'^admin/', include(admin.site.urls)),
) #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )