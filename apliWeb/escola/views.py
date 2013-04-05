# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from escola.models import Escole, Reglament, Equip, Calendari

def mainpage(request):
	#print "views.py: mainpage(" + str(request)+")"
	template = get_template('mainpage.html')
	variables = Context({
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Calendari',
	'optionmenu4': 'Equip',
	})

	output = template.render(variables)
	return HttpResponse(output)


def escola(request):
	#template = get_template(escola.html)
	#variables = Context({
	escola = Escole.objects.all()
	#html = "<html><body>Prova de projecte</body></html>",
	return render_to_response('escola.html',{'escola ': "hola"})
	

	#output = template.render(variables)
	#return HttpResponse(request)

def reglament(request):


	reglament = Reglament.objects.all()
	return render_to_response('base.html',{'reglament ': reglament})


