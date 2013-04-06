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


#def base(request):

#	variables = Context({
#	'titlehead': 'Escola aPP',
#	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
#	'contentbody': 'Manager per a la gestio de l`Escola',
#	'optionmenu1': 'Escola',
#	'optionmenu2': 'Reglament',
#	'optionmenu3': 'Equip',
#	'optionmenu4': 'Instalacions',

#	})

#	return render_to_response('base.html',variables)


def escola(request):
	escola = Escole.objects.all()
	variables = {
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'escola': escola
	}

	
	
	return render_to_response('escola.html',variables)

	

def reglament(request):
	reglament = Reglament.objects.all()
	variables = Context({
	'titlehead': 'Escola aPP',
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
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'equip' : equip
	})

	return render_to_response('equip.html',variables)

def instalacions(request):
	instalacions = Instalacion.objects.all()
	variables = Context({
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'instalacions': instalacions
	})

	return render_to_response('instalacions.html',variables)

def detallescoles(request):
	detallescoles = detallescoles.objects.all()
	variables = Context({
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'detallescoles': detallescoles,
	})

	return render_to_response('detallescoles.html',variables)

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

