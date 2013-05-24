from django.forms import ModelForm
from models	import Escole, Reglament, Equip, Instalacion

class	EscolaForm(ModelForm):
	class	Meta:
		model	=	Escole
		exclude	=	('user', 'date',)
class	EquipForm(ModelForm):
	class	Meta:
		model	=	Equip
		exclude	=	('imatge', 'user', 'date',)

class	ReglamentForm(ModelForm):
	class	Meta:
		model	=	Reglament
		exclude	=	('user', 'date',)

class	InstalacionForm(ModelForm):
	class	Meta:
		model	=	Instalacion
		exclude	=	('user', 'date',)
