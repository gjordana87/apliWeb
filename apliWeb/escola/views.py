# Create your views here.
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import Context,RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from escola.models import Escole, Reglament, Equip, Instalacion
#from django.contrib.auth import login, logout, authenticate
#from escola.forms import LoginForm
#from django.core.mail import EmailMultiAlternatives

def mainpage(request):
	template = get_template('base.html')
	variables = Context({
	'titlehead': 'Escola aPP',
	'pagetitle': 'Gestio Escoles de Futbol',
	'optionmenu1': 'Escoles',
	'optionmenu2': 'Reglaments',
	'optionmenu3': 'Equips',
	'optionmenu4': 'Instalacions',
	'user': request.user

	})
	output = template.render(variables)
	return HttpResponse(output)
	
def escola(request):
	escola = Escole.objects.all()
	context = RequestContext(request)
	variables = {
	'titlehead': 'Escoles',
	'pagetitle': 'Gestio Escoles de Futbol',
	'optionmenu1': 'Escoles',
	'optionmenu2': 'Reglaments',
	'optionmenu3': 'Equips',
	'optionmenu4': 'Instalacio',

	'escoles': escola
	}
	return render_to_response('escola.html',variables, context)

def reglament(request):
	reglament = Reglament.objects.all()
	context = RequestContext(request)
	variables = {
	'titlehead': 'Reglaments',
	'pagetitle': 'Gestio Escoles de Futbol',
	'optionmenu1': 'Escoles',
	'optionmenu2': 'Reglaments',
	'optionmenu3': 'Equips',
	'optionmenu4': 'Instalacions',

	'reglament': reglament
	}

	return render_to_response('reglament.html',variables, context)

def equip(request):
	equip = Equip.objects.all()
	context = RequestContext(request)
	escola = Escole.objects.filter(equip=equip)
	variables = {
	'titlehead': 'Equips',
	'pagetitle': 'Gestio Escoles de Futbol',
	'optionmenu1': 'Escoles',
	'optionmenu2': 'Reglaments',
	'optionmenu3': 'Equips',
	'optionmenu4': 'Instalacions',
	'equips' : equip
	
    }
	return render_to_response('equip.html',variables,context)

def instalacions(request):
	instalacions = Instalacion.objects.all()
	context = RequestContext(request)
	variables = {
	'titlehead': 'Instalacions',
	'pagetitle': 'Gestio Escoles de Futbol',
	'optionmenu1': 'Escoles',
	'optionmenu2': 'Reglaments',
	'optionmenu3': 'Equips',
	'optionmenu4': 'Instalacions',
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
            'pagetitle': 'Gestio Escoles de Futbol',
            'optionmenu1': 'Escoles',
			'optionmenu2': 'Reglaments',
			'optionmenu3': 'Equips',
			'optionmenu4': 'Instalacions',

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
			'pagetitle': 'Gestio Escoles de Futbol',
			'optionmenu1': 'Escoles',
			'optionmenu2': 'Reglaments',
			'optionmenu3': 'Equips',
			'optionmenu4': 'Instalacions',
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
			'pagetitle': 'Gestio Escoles de Futbol',
			'optionmenu1': 'Escoles',
			'optionmenu2': 'Reglaments',
			'optionmenu3': 'Equips',
			'optionmenu4': 'Instalacions',

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
			'pagetitle': 'Gestio Escoles de Futbol',
			'optionmenu1': 'Escoles',
			'optionmenu2': 'Reglaments',
			'optionmenu3': 'Equips',
			'optionmenu4': 'Instalacions',



			#'detallreglament': detallreglament,
	}

	except Instalacion.DoesNotExist:
	 raise Http404
	context = RequestContext(request)
	return render_to_response('detallreglament.html',variables,context)


