#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Escole(models.Model):
	nom = models.CharField('Nom', max_length=20, help_text='Nom Escola')
	direccio = models.CharField('Direccio', max_length=40, help_text='Direccio de Escola')
	telf = models.IntegerField('Telefon', max_length=9, help_text='Telefon Escola')
	president = models.CharField('President', max_length=200, help_text='Nom del actual President')
	vicepresident = models.CharField('Vicepresident', max_length=200, help_text='Nom del actual Vicepresident')
	coordinador = models.CharField('Coordinador', max_length=200, help_text='Nom del actual Coordinador')
	
	def __unicode__(self):
		return self.nom

class Equip(models.Model):
	categoria = models.CharField('Categoria', max_length=15, help_text='Nom de la categoria')
	numjug = models.IntegerField('Num de Jugadors', help_text='Nombre de Jugadors')
	entrenador = models.CharField('Entrenador', max_length=200, help_text='Com es diu l`entrenador')
	imatge = models.ImageField(upload_to='escola', verbose_name='Imatge')
	possicio = models.IntegerField('Possicio', help_text='Possicio en la classificacio')
	punts = models.IntegerField('Punts Classificacio', max_length=2)
	fkEscole = models.ManyToManyField(Escole)

	def __unicode__ (self):
		return self.categoria
	

class Instalacion(models.Model):
	nom = models.CharField('Nom', max_length=20, help_text='Nom Escola')
	direccio = models.CharField('Direccio', max_length=40, help_text='Direccio de Escola')
	fkEscole = models.ForeignKey(Escole)

	def __unicode__(self):
		return self.nom
	

class Reglament(models.Model):
	numnorma = models.IntegerField('Norma', max_length=2)
	normes = models.CharField('Nom Norma', max_length=20)
	descrip = models.TextField('Descripcio', max_length=2000, help_text='Descripcio')
	fkEscole = models.ForeignKey(Escole)
	
	def __unicode__(self):
		return self.normes

class Calendari(models.Model):
	jornada = models.IntegerField('Numero Jornada', max_length=2, help_text='Numero de jornada')
	data = models.DateTimeField(default= datetime.now(), blank=True)
	fkEquip = models.ForeignKey(Equip)

	def __unicode__(self):
		return self.jornada


