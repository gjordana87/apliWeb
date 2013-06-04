import models
from django.contrib import admin
from escola.models import *

from escola.forms import *

admin.site.register(Escole)
admin.site.register(Equip)
admin.site.register(Instalacion)
admin.site.register(Reglament)
admin.site.register(Review)

