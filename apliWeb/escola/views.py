# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
#from django.contrib.auth.models import User

def mainpage(request):
    template = get_template('mainpage.html')
    variables = Context({
	'titlehead': 'Escola aPP',
	'pagetitle': 'Benvingut a l`aplicatiu de l`Escola',
	'contentbody': 'Manager per a la gestio de l`Escola',
	'optionmenu1': 'Escola',
	'optionmenu2': 'Reglament',
	'optionmenu3': 'Junta',
	'optionmenu4': 'Calendari',
	'optionmenu5': 'Classificacio',
	'optionmenu6': 'Equip'
	})
	
    output = template.render(variables)
    return HttpResponse(output)
