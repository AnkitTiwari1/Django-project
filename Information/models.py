from django.db import models

class information(models.Model):
	ename=models.CharField(max_length=100)
	emob=models.IntegerField()
	email=models.EmailField()
	eaadhar=models.IntegerField()
	esalary=models.IntegerField()

	def __str__(self):
		return self.name


		
