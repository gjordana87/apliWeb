from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Escole, Equip, Reglament, Instalacion
from django.db import IntegrityError


class EscolaSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='escola-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Escole
        fields = ('url','nom', 'direccio', 'telf', 'president', 'vicepresident', 'coordinador', 'user')

class EquipSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='equip-detail')
    fkEscole = HyperlinkedRelatedField(view_name='escola-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Equip
        fields = ('url', 'categoria', 'numjug', 'entrenador', 'possicio', 'punts', 'user', 'fkEscole')

class ReglamentSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='reglament-detail')
    fkEscole = HyperlinkedRelatedField(view_name='escola-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Reglament
        fields = ('url', 'numnorma', 'normes', 'descrip', 'user', 'fkEscole' )

class InstalacioSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='instalacio-detail')
    fkEscole = HyperlinkedRelatedField(view_name='escola-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Instalacion
        fields = ('url', 'nom', 'direccio',  'user', 'fkEscole' )


