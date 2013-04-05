# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from escola.models import Escole, Reglament, Equip, Instalacion

def mainpage(request):
	#print "views.py: mainpage(" + str(request)+")"
	template = get_template('base.html')
	variables = Context({
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',

	})

	output = template.render(variables)
	return HttpResponse(output)


def escola(request):
	
	variables = {
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',

	}

	escola = Escole.objects.all()
	#html = "<html><body>Prova de projecte</body></html>",
	#output = template.render(variables)
	return render_to_response('escola.html',variables)

	#output = template.render(variables)
	#return HttpResponse(request)

def reglament(request):

	variables = Context({
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',

	})

	reglament = Reglament.objects.all()

	return render_to_response('reglament.html',variables)

def equip(request):
	variables = Context({
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	})

	equip = Equip.objects.all()
	return render_to_response('equip.html',variables)

def instalacions(request):
	variables = Context({
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	})

	instalacions = Instalacion.objects.all()
	return render_to_response('instalacions.html',variables)

