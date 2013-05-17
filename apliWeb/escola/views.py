# Create your views here.
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import Context,RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from escola.models import Escole, Reglament, Equip, Instalacion
from forms import EscolaForm, EquipForm, ReglamentForm, InstalacionForm
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView

def mainpage(request):
	template = get_template('base.html')
	variables = Context({
	'titlehead': 'Escola aPP',
	'user': request.user

	})
	output = template.render(variables)
	return HttpResponse(output)


def ok(request):
	#escola = Escole.objects.all()
	context = RequestContext(request)
	variables = {
	'titlehead': 'ok',
	'ok': ok
	}
	return render_to_response('ok.html',variables, context)
	
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
			#'detallreglament': detallreglament,
	}

	except Instalacion.DoesNotExist:
	 raise Http404
	context = RequestContext(request)
	return render_to_response('detallreglament.html',variables,context)


class EscolaCreate(CreateView):
	model = Escole
	template_name = 'form.html'
	form_class = EscolaForm
	
	def	form_valid(self, form):
		form.instance.user = self.request.user
		return super(EscolaCreate, self).form_valid(form)


class EquipCreate(CreateView):
	model = Equip
	template_name = 'form.html'
	form_class = EquipForm

	def	form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.Escola = Escola.objects.get(id=self.kwargs['pk'])
		return super(EquipCreate, self).form_valid(form)
	#def delete(self):
	#	print"Delete myModel1 called"
	#	super (Equip, self).delete()

class ReglamentCreate(CreateView):
	model = Reglament
	template_name = 'form.html'
	form_class = ReglamentForm

	def	form_valid(self, form):
		form.instance.user = self.request.user
		#form.instance.Escola = Escola.objects.get(id=self.kwargs['pk'])
		return super(ReglamentCreate, self).form_valid(form)

class InstalacioCreate(CreateView):
	model = Instalacion
	template_name = 'form.html'
	form_class = InstalacionForm

	def	form_valid(self, form):
		form.instance.user = self.request.user
		#form.instance.Escola = Escola.objects.get(id=self.kwargs['pk'])
		return super(InstalacioCreate, self).form_valid(form)

def	review(request,	pk):
	escola	=	get_object_or_404(escola,pk=pk)	
	review	  =	 RestaurantReview(	
		rating=request.POST['rating'],
		comment=request.POST['comment'],
		user=request.user,
		escola=escola)
	review.save()
	return HttpResponseRedirect(reverse('escola:escola_detail',args=(escola.id,)))






  

  




