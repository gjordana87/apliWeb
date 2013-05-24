from django.conf.urls import patterns, include, url
from escola.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import DetailView, ListView, UpdateView, DeleteView

from django.conf.urls.defaults import *
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
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    #url(r'^register/$',register),
    #url(r'^logout/$', 'django.contrib.auth.views.logout',{ 'next_page' : '/'}),
    #url(r'^login/$','django.contrib.auth.views.login'),
    #url(r'^login/$',login),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
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


#web 2.0
   # Crear Escola, equip, reglament, instalacions 
    url(r'^escola/Crear/$',EscolaCreate.as_view(),  name='escola_create'),
    url(r'^equip/Crear/$',EquipCreate.as_view(),name='equip_create'),
    url(r'^reglament/Crear/$',ReglamentCreate.as_view(),name='reglament_create'),
    url(r'^instalacions/Crear/$',InstalacioCreate.as_view(),name='instalacio_create'),
    
    #url(r'^escola/delete/$',escola_delete,  name='escola_delete'),

   
    #   Edit    restaurant  details,    ex.:/myrestaurants/restaurants/1/edit/
    url(r'^escola/(?P<pk>\d+)/edit/$',UpdateView.as_view(model = Escole,template_name = 'form.html',form_class = EscolaForm),name='escola_edit'),
    url(r'^equip/(?P<pk>\d+)/edit/$',UpdateView.as_view(model = Equip,template_name = 'form.html',form_class = EquipForm),name='equip_edit'),
    url(r'^instalacions/(?P<pk>\d+)/edit/$',UpdateView.as_view(model = Instalacion,template_name = 'form.html',form_class = InstalacionForm),name='install_edit'),
    url(r'^reglament/(?P<pk>\d+)/edit/$',UpdateView.as_view(model = Reglament,template_name = 'form.html',form_class = ReglamentForm),name='reglament_edit'),

    #Delete 
    #url(r'^escola/(?P<pk>\d+)/delete/$',DeleteView.as_view(),name='escola_delete'),
    url(r'^escola/(?P<pk>\d+)/delete/$',DeleteView.as_view(model= Escole, template_name='delete.html',success_url = '/escola'),name='escola_delete'),
    url(r'^equip/(?P<pk>\d+)/delete/$',DeleteView.as_view(model= Equip, template_name='delete.html',success_url = '/equip'),name='equip_delete'),
    url(r'^instalacions/(?P<pk>\d+)/delete/$',DeleteView.as_view(model= Instalacion, template_name='delete.html',success_url = '/instalacions'),name='install_delete'),
    url(r'^reglament/(?P<pk>\d+)/delete/$',DeleteView.as_view(model= Reglament, template_name='delete.html',success_url = '/reglament'),name='reglament_delete'),

    url(r'^equip/(?P<pk>\d+)/reviews/create/$','escola.views.review', name='equip_create'),

    url(r'^admin/', include(admin.site.urls)),
) #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )