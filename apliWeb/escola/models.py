#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.urlresolvers import reverse	
 
class Escole(models.Model):
	nom = models.CharField('Nom', max_length=20, help_text='Nom Escola')
	direccio = models.CharField('Direccio', max_length=40, help_text='Direccio de Escola')
	telf = models.IntegerField('Telefon', max_length=9, help_text='Telefon Escola')
	president = models.CharField('President', max_length=200, help_text='Nom del actual President')
	vicepresident = models.CharField('Vicepresident', max_length=200, help_text='Nom del actual Vicepresident')
	coordinador = models.CharField('Coordinador', max_length=200, help_text='Nom del actual Coordinador')
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=date.today)
	
	def __unicode__(self):
		return u"%s" % self.nom
	def get_absolute_url(self):
		return reverse('detail_escola',kwargs={'idEscole':self.pk})
	def get_default_user():
		return User.objects.get(pk=1)


class Equip(models.Model):
	categoria = models.CharField('Categoria', max_length=15, help_text='Nom de la categoria')
	numjug = models.IntegerField('Num de Jugadors', help_text='Nombre de Jugadors')
	entrenador = models.CharField('Entrenador', max_length=200, help_text='Com es diu l`entrenador')
	imatge = models.ImageField(upload_to='static/files', verbose_name='Imatge')
	possicio = models.IntegerField('Possicio', help_text='Possicio en la classificacio')
	punts = models.IntegerField('Punts Classificacio', max_length=2)
	fkEscole = models.ForeignKey(Escole)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=date.today)

	def __unicode__ (self):
		return u"%s" % self.categoria
	def get_absolute_url(self):
		return reverse('detail_equip',kwargs={'idEquip':self.pk})
	def get_default_user():
		return User.objects.get(pk=1)
	

class Instalacion(models.Model):
	nom = models.CharField('Nom', max_length=20, help_text='Nom Escola')
	direccio = models.CharField('Direccio', max_length=40, help_text='Direccio de Escola')
	fkEscole = models.ForeignKey(Escole)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=date.today)

	def __unicode__(self):
		return u"%s" % self.nom
	def get_absolute_url(self):
		return reverse('detail_instal',kwargs={'idInstalacions':self.pk})
	def get_default_user():
		return User.objects.get(pk=1)
	

class Reglament(models.Model):
	numnorma = models.IntegerField('Norma', max_length=2)
	normes = models.CharField('Nom Norma', max_length=20)
	descrip = models.TextField('Descripcio', max_length=2000, help_text='Descripcio')
	fkEscole = models.ForeignKey(Escole)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	date = models.DateField(default=date.today)
	
	def __unicode__(self):
		return u"%s" % self.normes
	def get_absolute_url(self):
		return reverse('detail_regla',kwargs={'idReglament':self.pk})
	def get_default_user():
		return User.objects.get(pk=1)


class Review(models.Model):
    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class PartitReview(Review):
    Equip = models.ForeignKey(Equip)
