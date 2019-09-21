from django.db import models

# Create your models here.
class Random(models.Model):
	Random_chislo = models.CharField('Рандомное число которое нужно получить', max_length= 200)

	def __str__(self):
		return self.Random_chislo
	class Meta():
		verbose_name = 'Рандомное число которое нужно'
		verbose_name_plural= 'Рандомное число которое нужно'