# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from escola.models import Escole, Reglament, Equip, Instalacion
from escola import *


def mainpage(request):
	template = get_template('base.html')
	variables = Context({
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'user': request.user

	})

	return render_to_response(
		'base.html', {
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'user': request.user

	})
	
def escola(request):
	escola = Escole.objects.all()
	variables = {
	'titlehead': 'Escoles',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'escoles': escola
	}

	
	
	return render_to_response('escola.html',variables)

	

def reglament(request):
	reglament = Reglament.objects.all()
	variables = Context({
	'titlehead': 'Reglaments',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'reglament': reglament
	})


	return render_to_response('reglament.html',variables)

def equip(request):
	
	equip = Equip.objects.all()
	variables = Context({
	'titlehead': 'Equips',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'equips' : equip
	})
	return render_to_response('equip.html',variables)

def instalacions(request):
	instalacions = Instalacion.objects.all()
	variables = Context({
	'titlehead': 'Instalacions',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'instalacions': instalacions
	})

	return render_to_response('instalacions.html',variables)

#def detallescoles(request):
#	detallescoles = detallescoles.objects.all()
#	variables = Context({
#	'titlehead': 'Escola aPP',
#	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
#	'contentbody': 'Manager per a la gestio de l`Escola',
#	'optionmenu1': 'Escola',
#	'optionmenu2': 'Reglament',
#	'optionmenu3': 'Equip',
#	'optionmenu4': 'Instalacions',
#	'detallescoles': detallescoles,
#	})

#	return render_to_response('detallescoles.html',variables	)

def detallescoles(request):
	try:
		escola = Escole.objects.get(name=detallescoles)
		variables = ({
		'titlehead':"Detall de escoles",
		'nom': escola.nom,
		'direccio': escola.direccio,
		'telf': escola.telf,
		'president': escola.president,
		'vicepresident': escola.vicepresident,
		'coordinador': escola.coordinador,
		})
	except Escole.DoesNotExist:
		raise Http404
		return render_to_response(detallescoles.html, variables)

def detallequips(request):
	detallequips = detallequips.objects.all()
	variables = Context({
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'detallequips': detallequips,
	})

	return render_to_response('detallequips.html',variables)

