from django.forms import ModelForm
from models	import Escole, Reglament, Equip, Instalacion

class	EscolaForm(ModelForm):
	class	Meta:
		model	=	Escole
class	EquipForm(ModelForm):
	class	Meta:
		model	=	Equip
		exclude	=	('imatge')

class	ReglamentForm(ModelForm):
	class	Meta:
		model	=	Reglament

class	InstalacionForm(ModelForm):
	class	Meta:
		model	=	Instalacion

#class DeleteNewForm(forms.ModelForm):
#	class Meta:
#		model = New
#		fields= []