# Create your views here.
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.core.exceptions import PermissionDenied
from django.template import Context,RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from django.contrib import auth
from escola.models import Escole, Reglament, Equip, Instalacion, Review
from forms import EscolaForm, EquipForm, ReglamentForm, InstalacionForm
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from serializers import EscolaSerializer, EquipSerializer, ReglamentSerializer, InstalacioSerializer, EquipReviewSerializer

class ControlLogin(object):

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(ControlLogin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
	def get_object(self, *args, **kwargs):
		obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
		if not obj.user == self.request.user:
			raise PermissionDenied
		return obj
  
def mainpage(request):
	template = get_template('base.html')
	variables = Context({
	'titlehead': 'Escola aPP',
	'user': request.user

	})
	output = template.render(variables)
	return HttpResponse(output)
	
def escola(request):
	escola = Escole.objects.all()
	context = RequestContext(request)
	variables = {
	'titlehead': 'Escoles',
	'escoles': escola
	}

	return render_to_response('escola.html',variables, context)

def reglament(request):
	reglament = Reglament.objects.all()
	context = RequestContext(request)
	variables = {
	'titlehead': 'Reglaments',
	'reglament': reglament
	}

	return render_to_response('reglament.html',variables, context)

def equip(request):
	equip = Equip.objects.all()
	context = RequestContext(request)
	escola = Escole.objects.filter(equip=equip)
	variables = {
	'titlehead': 'Equips',	
	'equips' : equip
	
    }
	return render_to_response('equip.html',variables,context)

def instalacions(request):
	instalacions = Instalacion.objects.all()
	context = RequestContext(request)
	variables = {
	'titlehead': 'Instalacions',	
	'instalacions': instalacions
    }
	return render_to_response('instalacions.html', variables,context)



def detallescoles(request,idEscole):
	try:
            escola = Escole.objects.get(pk=idEscole)
            variables = {
            'titlehead':"Detall de escoles",
            'nom': escola.nom,
            'direccio': escola.direccio,
            'telf': escola.telf,
            'president': escola.president,
            'vicepresident': escola.vicepresident,
            'coordinador': escola.coordinador,
            'idEscole': idEscole,

            #'detallescoles': detallescoles
	}

	except Escole.DoesNotExist:
	 raise Http404
	context = RequestContext(request)
	return render_to_response('detallescoles.html', variables, context)

def detallequips(request,idEquip):
	try:

			equip = Equip.objects.get(pk=idEquip)
			variables = {
			'titlehead': 'Detall equip ',
			'categoria': equip.categoria,
			'numjug': equip.numjug,
			'entrenador': equip.entrenador,
			'imatge': equip.imatge,
			'possicio': equip.possicio,
			'punts': equip.punts,
			'escola': equip.fkEscole,
			'detallequips': detallequips,
			'RATING_CHOICES': Review.RATING_CHOICES,
			
			'idEquip': idEquip,
	}
	except Equip.DoesNotExist:
	 raise Http404
	context = RequestContext(request)
	return render_to_response('detallequips.html',variables, context)

def detallinstall(request, idInstalacions):
	try:
		
			instalacion = Instalacion.objects.get(pk=idInstalacions)
			variables = {
			'titlehead': 'Detall de les Instalacions',
			'nom': instalacion.nom,
			'direccio': instalacion.direccio,
			'escola': instalacion.fkEscole,
			'idInstalacions': idInstalacions,
			#'detallinstall': detallinstall,
	}

	except Instalacion.DoesNotExist:
	 raise Http404
	context = RequestContext(request)
	return render_to_response('detallinstall.html',variables,context)

def detallreglament(request,idReglament):
	try:
		
			reglament = Reglament.objects.get(pk=idReglament)
			variables = {
			'titlehead': 'Detall de les Instalacions',
			'numnorma': reglament.numnorma,
			'normes': reglament.normes,
			'descripcio': reglament.descrip,
			'escola': reglament.fkEscole,
			'idReglament': idReglament,	
			#'detallreglament': detallreglament,
	}

	except Instalacion.DoesNotExist:
	 raise Http404
	context = RequestContext(request)
	return render_to_response('detallreglament.html',variables,context)

#Per crear entitats a la taula corresponent de la base de dades
class EscolaCreate(ControlLogin, CreateView):
	model = Escole
	template_name = 'form.html'
	form_class = EscolaForm
	
	def	form_valid(self, form):
		form.instance.user = self.request.user
		return super(EscolaCreate, self).form_valid(form)

class EquipCreate(ControlLogin, CreateView):
	model = Equip
	template_name = 'form.html'
	form_class = EquipForm

	def	form_valid(self, form):
		form.instance.user = self.request.user
		return super(EquipCreate, self).form_valid(form)

class ReglamentCreate(ControlLogin, CreateView):
	model = Reglament
	template_name = 'form.html'
	form_class = ReglamentForm

	def	form_valid(self, form):
		form.instance.user = self.request.user
		return super(ReglamentCreate, self).form_valid(form)

class InstalacioCreate(ControlLogin, CreateView):
	model = Instalacion
	template_name = 'form.html'
	form_class = InstalacionForm

	def	form_valid(self, form):
		form.instance.user = self.request.user
		return super(InstalacioCreate, self).form_valid(form)

#reviews
@login_required()
def EquipReview(request, pk):
    equip = get_object_or_404(Equip, pk=pk)
    equip = EquipReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        equip=equip)
    review.save()
    return HttpResponseRedirect(urlresolvers.reverse('equip_detail', args=(equip.id,)))


#Per borrar entitats de les taules de la base de dades
class EscolaDelete(ControlLogin, DeleteView):
	model = Escole 
	template_name = 'delete.html'
	success_url = '/escoles'

class EquipDelete(ControlLogin, DeleteView):
	model = Equip 
	template_name = 'delete.html'
	success_url = '/equip'

class ReglamentDelete(ControlLogin, DeleteView):
	model = Reglament 
	template_name = 'delete.html'
	success_url = '/reglament'

class InstalacioDelete(ControlLogin, DeleteView):
	model = Instalacion 
	template_name = 'delete.html'
	success_url = '/instalacions'


### RESTful API views ###
class APIEscolaList(generics.ListCreateAPIView):
	model = Escole
	serializer_class = EscolaSerializer

class APIEscolaDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Escole
	serializer_class = EscolaSerializer


class APIEquipDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Equip
	serializer_class = EquipSerializer

class APIEquipList(generics.ListCreateAPIView):
	model = Equip
	serializer_class = EquipSerializer

class APIReglamentDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Reglament
	serializer_class = ReglamentSerializer

class APIReglamentList(generics.ListCreateAPIView):
	model = Reglament
	serializer_class = ReglamentSerializer


class APIInstalacioDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Instalacion
	serializer_class = InstalacioSerializer

class APIInstalacioList(generics.ListCreateAPIView):
	model = Instalacion
	serializer_class = InstalacioSerializer


class APIEquipReviewDetail(generics.ListCreateAPIView):
	model = Equip
	serializer_class = EquipReviewSerializer