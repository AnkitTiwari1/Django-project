from django.db import models

# Create your models here.
class post(models.Model):
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=100)
	date=models.DateField(auto_now_add=True)
	post=models.TextField()
	file=models.FileField(blank=True)

	def __str__(self):
		return self.title


