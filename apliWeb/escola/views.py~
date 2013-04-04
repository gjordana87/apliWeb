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
	})
	
    output = template.render(variables)
    return HttpResponse(output)
