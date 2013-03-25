# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Escola(models.Model):
	equip = models.CharField(max_length=200)
	junta = models.CharField(max_length=200)
	
	def __unicode__ (self):
		return self.equip
	

class Instalacio(models.Model):
	vestidor = models.TextField(max_length=200)
	camp = models.TextField(max_length=200)
	
	def __unicode__(self):
		return self.vestidor
	

class Reglament(models.Model):
	bases = models.TextField(max_length=2000)
	
	def __unicode__(self):
		return self.base

class Calendari(models.Model):
	#data = 
	partit = models.CharField(max_length=200)
	#hora =

	def __unicode__(self):
		return self.partit

#class Classificacio(models.Models):
	
