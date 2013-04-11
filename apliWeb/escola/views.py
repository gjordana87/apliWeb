# Create your views here.
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.template import Context,RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from escola.models import Escole, Reglament, Equip, Instalacion
from escola import *
from django.contrib.auth import login, logout, authenticate
from escola.forms import LoginForm
#from django.core.mail import EmailMultiAlternatives

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
	output = template.render(variables)
	return HttpResponse(output)


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
	return render_to_response()

	
def escola(request):
	escola = Escole.objects.all()
	variables = {
	'titlehead': 'Escoles',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'InstalacioLoginFormLoginFormns',
	'escoles': escola
	}
	return render_to_response('escola.html',variables)

def reglament(request):
	reglament = Reglament.objects.all()
	variables = {
	'titlehead': 'Reglaments',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'reglament': reglament
	}

	return render_to_response('reglament.html',variables)

def equip(request):
	equip = Equip.objects.all()
	variables = {
	'titlehead': 'Equips',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
	'equips' : equip
    }
	return render_to_response('equip.html',variables)

def instalacions(request):
	instalacions = Instalacion.objects.all()
	variables = {
	'titlehead': 'Instalacions',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Equip',
	'optionmenu4': 'Instalacions',
    'instalacions': instalacions
    }
	return render_to_response('instalacions.html', variables)

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
            'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
            'contentbody': 'Manager per a la gestio de l`Escola',
            'optionmenu1': 'Escola',
			'optionmenu2': 'Reglament',
			'optionmenu3': 'Equip',
			'optionmenu4': 'Instalacions',
            #'detallescoles': detallescoles
	}

	except Escole.DoesNotExist:
	 raise Http404
	return render_to_response('detallescoles.html', variables)

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
			'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
			'contentbody': 'Manager per a la gestio de l`Escola',
			'optionmenu1': 'Escola',
			'optionmenu2': 'Reglament',
			'optionmenu3': 'Equip',
			'optionmenu4': 'Instalacions',
			#'detallequips': detallequips,
	}
	except Equip.DoesNotExist:
	 raise Http404
	return render_to_response('detallequips.html',variables)

def detallinstall(request, idInstalacions):
	try:
		
			instalacion = Instalacion.objects.get(pk=idInstalacions)
			variables = {
			'titlehead': 'Detall de les Instalacions',
			'nom': instalacion.nom,
			'direccio': instalacion.direccio,
	
			'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
			'contentbody': 'Manager per a la gestio de l`Escola',
			'optionmenu1': 'Escola',
			'optionmenu2': 'Reglament',
			'optionmenu3': 'Equip',
			'optionmenu4': 'Instalacions',
			#'detallinstall': detallinstall,
	}

	except Instalacion.DoesNotExist:
	 raise Http404
	return render_to_response('detallinstall.html',variables)

def base(request):
	template = get_template('base.xml')
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

	return render_to_response('base.xml',variables)

def detallreglament(request,idReglament):
	try:
		
			reglament = Reglament.objects.get(pk=idReglament)
			variables = {
			'titlehead': 'Detall de les Instalacions',
			'numnorma': reglament.numnorma,
			'normes': reglament.normes,
			'descripcio': reglament.descrip,
			'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
			'contentbody': 'Manager per a la gestio de l`Escola',
			'optionmenu1': 'Escola',
			'optionmenu2': 'Reglament',
			'optionmenu3': 'Equip',
			'optionmenu4': 'Instalacions',
			#'detallreglament': detallreglament,
	}

	except Instalacion.DoesNotExist:
	 raise Http404
	return render_to_response('detallreglament.html',variables)




def login_view(request):

	missatge = ""
	if request.user.is_authenticated():
			return HttpResponseRedirect('/')
	else:
				if request.method == "POST":
					form = LoginForm(request.POST)
					if form.is_valid():
							username = form.cleaned_data['username']
							password = form.cleaned_data['password']
							usuari = authenticate(username=username,password=password)
							if usuari is not None and usuari.is_active:
									login(request,usuari)
									return HttpResponseRedirect('/')
							else:
									missatge = "Usuari i/o password incorrecte"
				form = LoginForm()
				ctx = {'form':form,'missatge':missatge}
				return render_to_response('login.html',ctx,context_instance=RequestContext(request))	

def logout_view(request):

	logout(request)
	return HttpResponseRedirect('/')					